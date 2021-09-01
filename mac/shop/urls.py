from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path("",views.index,name="shophome"),
    path("/about",views.about,name="about"),
    path("/contactus",views.contactus,name="contactus"),
    path("/tracker",views.tracker,name="tracker"),
    path("/productview/<int:myid>",views.productview,name="productview"),
    path("/search/",views.search,name="search"),
    path("/checkout",views.checkout,name="checkout"),
    path("/menn",views.menn,name="menn"),
    path("/womenn",views.womenn,name="womenn"),
    path("/accessory",views.accessory,name="accessory"),
    path("/login", views.login, name="login"),
    path("/menview/<int:myid>",views.menview,name="menview"),
    path("/womenview/<int:myid>",views.womenview,name="womenview"),
    path("/accessoryview/<int:myid>",views.accessoryview,name="accessoryview"),

]

