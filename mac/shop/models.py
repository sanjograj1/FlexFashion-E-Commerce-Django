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
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=70, default="")
    number = models.CharField(max_length=70, default="")


    def __str__(self):
        return self.name