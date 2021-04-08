from django.utils import timezone
from django.db import models


# Create your models here.
class Customer(models.Model):
    cust_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=50)

    def __str__(self):
        return str(self.cust_name)


# class Itemtype(models.Model):
#     item_type = models.CharField(max_length=20)
#
#     def __str__(self):
#         return str(self.item_type)
choice = (
    ('maincourse', 'MAINCOURSE'),
    ('appetizer','APPETIZER'),
    ('salad','SALAD'),
    ('desserts', 'DESSERTS'),
    ('beverage','BEVERAGE'),
)

class Item(models.Model):
    #item_type = models.ForeignKey(Itemtype, on_delete=models.CASCADE)
    item_type= models.CharField(max_length=30, choices=choice, null=False)
    item_name = models.CharField(max_length=50)
    description = models.CharField(max_length=100, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_date = models.DateField(default=timezone.now)

    def __str__(self):
        return str(self.item_name)



# Create your models here.
class OrderDetail(models.Model):
   Customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='OrderDetail')
   order_status = models.CharField(max_length=50)

   def __str__(self):
       return str(self.order_status)


# Create your models here.
class Payment(models.Model):
   Customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='Payment')
   payment_status = models.CharField(max_length=50)
   address = models.CharField(max_length=200)
   date = models.DateField(default=timezone.now, blank=True, null=True)

   def __str__(self):
       return str(self.Customer)



