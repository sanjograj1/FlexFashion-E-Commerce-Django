from django.db import models

# Create your models here.
class product(models.Model):
    product_id=models.AutoField
    category=models.CharField(max_length=50,default="")
    price=models.IntegerField(default=0)
    product_name=models.CharField(max_length=30)
    desc=models.CharField(max_length=50)
    date=models.DateField()
    image=models.ImageField(upload_to='shop/images',default="")

    def __str__(self):
        return self.product_name

class Contact(models.Model):

    name = models.CharField(max_length=50)
    email = models.CharField(max_length=70, default="")
    number = models.CharField(max_length=70, default="")


    def __str__(self):
        return self.name

class Order(models.Model):

    items=models.CharField(max_length=1000)
    city=models.CharField(max_length=40)
    zip=models.CharField(max_length=30)
    name = models.CharField(max_length=50)
    state = models.CharField(max_length=30)
    phone=models.IntegerField(default="")
    email = models.EmailField(max_length=50)
    address = models.CharField(max_length=90)

class updateorder(models.Model):
    orderId=models.IntegerField(default="")

    updatedesc=models.CharField(max_length=300)
    time=models.DateField(auto_now_add=True)

class men(models.Model):
    product_id=models.AutoField
    category=models.CharField(max_length=50,default="")
    price=models.IntegerField(default=0)
    product_name=models.CharField(max_length=30)
    desc=models.CharField(max_length=50)
    date=models.DateField()
    image=models.ImageField(upload_to='shop/images',default="")

class women(models.Model):
    product_id=models.AutoField
    category=models.CharField(max_length=50,default="")
    price=models.IntegerField(default=0)
    product_name=models.CharField(max_length=30)
    desc=models.CharField(max_length=50)
    date=models.DateField()
    image=models.ImageField(upload_to='shop/images',default="")

class accessories(models.Model):
    product_id=models.AutoField
    category=models.CharField(max_length=50,default="")
    price=models.IntegerField(default=0)
    product_name=models.CharField(max_length=30)
    desc=models.CharField(max_length=50)
    date=models.DateField()
    image=models.ImageField(upload_to='shop/images',default="")