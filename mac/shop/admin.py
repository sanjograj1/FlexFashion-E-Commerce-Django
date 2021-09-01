from django.contrib import admin
from .models import product,Contact,Order,updateorder,men,women,accessories
# Register your models here.
admin.site.register(product)
admin.site.register(Contact)
admin.site.register(Order)
admin.site.register(updateorder)
admin.site.register(men)
admin.site.register(women)
admin.site.register(accessories)