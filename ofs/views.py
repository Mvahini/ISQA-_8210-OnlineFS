from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import *
from .forms import *
from .forms import SignUpForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from . models import Item, OrderDetail
from math import ceil
import json


now = timezone.now()

def home(request):
   return render(request, 'ofs/home.html',
                 {'ofs': home})

def login(request):
    return render(request, 'registration/login.html',
                 {})


class SignUpView(CreateView):
    form_class = SignUpForm   # After Creating Login Form Then Put 'login' Here.
    template_name = 'registration/register.html'

    def form_valid(self, form):
        form.save()
        return redirect('ofs:home')

def index(request):
    allitems = []
    catprods = Item.objects.values('category')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prod = Item.objects.filter(category=cat)
        n = len(prod)  # length of products
        nSlides = n//4 + ceil((n/4)-(n//4))   # Number of slides
        allitems.append([prod, range(1, nSlides), nSlides])

    context = {'all_items':allitems}
    return render(request, 'ofs/index.html', context)


@login_required
def maincourse_list(request):
    maincourse = Item.objects.filter(created_date__lte=timezone.now(), item_type='maincourse')
    return render(request, 'ofs/maincourse_list.html',
                 {'maincourses': maincourse})

@login_required
def appetizer_list(request):
    appetizer = Item.objects.filter(created_date__lte=timezone.now(), item_type='appetizer')
    return render(request, 'ofs/appetizer_list.html',
                 {'appetizers': appetizer})


@login_required
def salad_list(request):
    salad = Item.objects.filter(created_date__lte=timezone.now(), item_type='salad')
    return render(request, 'ofs/salad_list.html',
                 {'salads': salad})



@login_required
def desserts_list(request):
    desserts = Item.objects.filter(created_date__lte=timezone.now(), item_type='desserts')
    return render(request, 'ofs/desserts_list.html',
                 {'desserts': desserts})


@login_required
def beverage_list(request):
    beverage = Item.objects.filter(created_date__lte=timezone.now(), item_type='beverage')
    return render(request, 'ofs/beverage_list.html',
                 {'beverages': beverage})



def contact (request):
    return render(request,'registration/contact.html')


def checkout(request):
    if request.method == "POST":
        name = request.POST.get('name', '')
        amount = request.POST.get('amount', '')
        email = request.POST.get('email', '')
        address = request.POST.get('address1', '') + " " + request.POST.get('address2', '')
        city = request.POST.get('city', '')
        state = request.POST.get('state', '')
        zip_code = request.POST.get('zip_code', '')
        phone = request.POST.get('phone', '')
        OrderDetail = models.OrderDetail(name=name, amount=amount, email=email, address=address, city=city,
                       state=state, zip_code=zip_code, phone=phone)
        OrderDetail.save()
        update = OrderDetail(ordered_by=OrderDetail, update_desc="The order has been placed")
        update.save()
        thank = True
        # return render(request, 'shop/checkout.html', {'thank':thank, 'id': id})
        param_dict = {

            'MID': 'VMLskh33374131769871',  # WorldP64425807474247  # VMLskh33374131769871
            'TXN_AMOUNT': str(amount),
            'CUST_ID': email,  # 'acfff@paytm.com'
            'INDUSTRY_TYPE_ID': 'Retail',
            'WEBSITE': 'WEBSTAGING',
            'CHANNEL_ID': 'WEB',

        }
        # param_dict['CHECKSUMHASH'] = Checksum.generate_cheo_id = OrderDetail.objects.only('OrderDetail_id')
        return render(request, 'ofs/payment.html', {'param_dict': param_dict, })

    return render(request, 'ofs/checkout.html')


def forgot_password(request):
    if request.method == 'POST':
        return render(request, 'templates/registration/password_reset_complete.html')
    else:
        return render(request, 'templates/registration/password_reset_complete.html')


def about(request):
    return render(request, 'registration/about.html')