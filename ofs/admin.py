from django.contrib import admin

from .models import Customer,Appetizer,Salad,Dessert,OrderDetail,Payment

class CustomerList(admin.ModelAdmin):
    list_display = ( 'cust_name', 'email', 'phone_number' )
    list_filter = ( 'cust_name', 'email')
    search_fields = ('cust_name', )
    ordering = ['cust_name']


admin.site.register(Customer)

class AppetizerList(admin.ModelAdmin):
    list_display = ( 'appetizer_name', 'description', 'price' )
    list_filter = ( 'appetizer_name', 'description')
    search_fields = ('appetizer_name', )
    ordering = ['appetizer_name']


admin.site.register(Appetizer)

class SaladList(admin.ModelAdmin):
    list_display = ( 'salad_name', 'description', 'price' )
    list_filter = ( 'salad_name', 'description')
    search_fields = ('salad_name', )
    ordering = ['salad_name']


admin.site.register(Salad)

class DessertList(admin.ModelAdmin):
    list_display = ( 'dessert_name', 'description', 'price' )
    list_filter = ( 'dessert_name', 'description')
    search_fields = ('dessert_name', )
    ordering = ['dessert_name']


admin.site.register(Dessert)

class OrderDetailtList(admin.ModelAdmin):
    list_display = ( 'Customer', 'order_status')
    list_filter = ( 'Customer', 'order_status')
    search_fields = ('Customer', )
    ordering = ['Customer']


admin.site.register(OrderDetail)

class PaymentList(admin.ModelAdmin):
    list_display = ( 'Customer', 'payment_status', 'address')
    list_filter = ( 'Customer', 'payment_status')
    search_fields = ('Customer', )
    ordering = ['Customer']


admin.site.register(Payment)