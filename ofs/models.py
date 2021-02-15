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

# Create your models here.
class Appetizer(models.Model):
    appetizer_name = models.CharField(max_length=50)
    description = models.CharField(max_length=100, blank=True)
    price = models.FloatField()

    def __str__(self):
        return str(self.appetizer_name)


# Create your models here.
class Salad(models.Model):
    salad_name = models.CharField(max_length=50)
    description = models.CharField(max_length=100, blank=True)
    price = models.FloatField()

    def __str__(self):
        return str(self.salad_name)


# Create your models here.
class Dessert(models.Model):
    dessert_name = models.CharField(max_length=50)
    description = models.CharField(max_length=100, blank=True)
    price = models.FloatField()

    def __str__(self):
        return str(self.dessert_name)




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