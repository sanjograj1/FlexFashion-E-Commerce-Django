from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import product,Contact,Order,updateorder
from django.contrib import messages
from math import ceil
import json


def index(request):
    pros=product.objects.all()
    n=len(pros)
    slides=n//4 +ceil((n/4)-(n//4))
    allprods=[]
    cats=product.objects.values('category','id')
    cat={item['category'] for item in cats}
    for cat in cat:
        pro = product.objects.filter(category=cat)
        print(pro)
        n = len(pro)
        slides = n // 4 + ceil((n / 4) - (n // 4))

        allprods.append([pro,range(0,slides),slides])
    context={'allprods':allprods}
    return render(request,'shop/index.html',context)

def about(request):
    return render(request, 'shop/about.html')

def contactus(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        number = request.POST['number']
        contact = Contact(name=name, email=email, number=number)
        contact.save()
        print('use created')
        messages.info(request, "We'll get in touch with you soon.")
    return render(request, 'shop/contact us.html')

def productview(request,myid):
    pros = product.objects.filter(id=myid)
    print(pros)
    return render(request, 'shop/productview.html',{'pros':pros[0]})


def tracker(request):
    if request.method == 'POST':
        email = request.POST['email']
        orderId = request.POST['orderId']


        try:
            orders=Order.objects.filter(id=orderId,email=email)
            if len(orders)>0:
                update=updateorder.objects.filter(id=orderId)
                updates=[]
                for i in update:
                    updates.append({'text':i.updatedesc,'time':i.time})
                    response=json.dumps(updates,default=str)
                    return HttpResponse(response)

            else:
                return HttpResponse('error')
        except Exception as e:
            return HttpResponse("exception")

    return render(request, 'shop/tracker.html')

def search(request):
    return render(request, 'shop/search.html')

def checkout(request):
    if request.method == 'POST':
        email = request.POST['email']
        phone = request.POST['phone']
        address=request.POST['address']
        city = request.POST['city']
        zip = request.POST['zip']
        state = request.POST['state']
        items = request.POST['items']
        order = Order( email=email, phone=phone,address=address,city=city,zip=zip,state=state,items=items)
        order.save()
        update=updateorder(orderId=order.id,updatedesc="Your order has been placed")
        update.save()
        thank=True
        id=order.id
        print(id)
        return render(request, 'shop/checkout.html', {'thank': thank, 'id': id})
    return render(request, 'shop/checkout.html')


