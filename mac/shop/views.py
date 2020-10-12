from django.shortcuts import render
from django.http import HttpResponse
from .models import product,Contact
from math import ceil
def index(request):
    pros=product.objects.all()
    n=len(pros)
    slides=n//4 +ceil((n/4)-(n//4))
    allprods=[]
    cats=product.objects.values('category','id')


    cat={item['category'] for item in cats}
    for cat in cat:
        pro = product.objects.filter(category=cat)
        n = len(pro)
        slides = n // 4 + ceil((n / 4) - (n // 4))

        allprods.append([pro,range(0,slides),slides])
    context={'allprods':allprods}

    return render(request,'shop/index.html',context)
def about(request):
    return render(request, 'shop/about.html')
def contactus(request):
    if request.method=='POST':
        name=request.POST.get('name','')
        email= request.POST.get('email', '')
        number= request.POST.get('number', '')
        contact=Contact(name=name,email=email,number=number)
        contact.save()

    return render(request, 'shop/contact us.html')
def productview(request,myid):
    pros = product.objects.filter(id=myid)
    print(pros)

    return render(request, 'shop/productview.html',{'pros':pros[0]})
def tracker(request):
    return render(request, 'shop/tracker.html')
def search(request):
    return render(request, 'shop/search.html')
def checkout(request):
    return render(request, 'shop/checkout.html')


