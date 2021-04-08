from django.conf.urls import url
from . import views
from django.urls import path
from django.contrib.auth import views as auth_views
from .views import SignUpView
from django.urls import path, re_path

app_name = 'ofs'
urlpatterns = [
    path('', views.home, name='home'),
    re_path(r'^home/$', views.home, name='home'),
    path('', views.index, name='home'),

    #change password
    path('accounts/password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name = "registration/changedpassword.html"), name='changedpassword'),
    path('accounts/password_change/', auth_views.PasswordChangeView.as_view(template_name = "registration/changePassword.html"), name='changePassword'),
    #forgot password
    path('accounts/password_reset/', auth_views.PasswordResetView.as_view(template_name= "registration/forgot_password.html"), name='forgot_password'),
    path('accounts/password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name="registration/password_reset_done.html"), name='password_reset_done'),
    path('accounts/reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="registration/password_reset_confirm.html"), name='password_reset_confirm'),
    path('accounts/reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name="registration/password_reset_complete.html"), name='password_reset_complete'),

    path('register/', SignUpView.as_view(), name='register'),
    path('', views.maincourse_list, name='maincourse_list'),
    path('maincourse_list', views.maincourse_list, name='maincourse_list'),
    path('appetizer_list', views.appetizer_list, name='appetizer_list'),
    path('salad_list', views.salad_list, name='salad_list'),
    path('desserts_list', views.desserts_list, name='desserts_list'),
    path('beverage_list', views.beverage_list, name='beverage_list'),


    path('checkout/', views.checkout, name='checkout'),
    path('contact', views.contact, name='contact'),
    path('about/', views.about, name='about'),

]

