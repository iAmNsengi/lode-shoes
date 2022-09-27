from django.contrib import admin
from .models import *



class OrderAdmin(admin.ModelAdmin):
    list_display = ('client', 'product','order_date','order_status','ship_address')

class ClientAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email','username','address')

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')

class CartAdmin(admin.ModelAdmin):
    list_display = ('client', 'item','quantity','amount')
   
# Register your models here.
admin.site.register(Client,ClientAdmin)
admin.site.register(Product,ProductAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Cart, CartAdmin)
admin.site.register(ClientVerify)







