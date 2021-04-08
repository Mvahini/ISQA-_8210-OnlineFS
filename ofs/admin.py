from django.contrib import admin

from .models import Customer,OrderDetail,Payment, Item

class CustomerList(admin.ModelAdmin):
    list_display = ( 'cust_name', 'email', 'phone_number' )
    list_filter = ( 'cust_name', 'email')
    search_fields = ('cust_name', )
    ordering = ['cust_name']


admin.site.register(Customer)



admin.site.register(Item)

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

