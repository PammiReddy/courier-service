
from django.urls import path
from . import views

urlpatterns = [
    path('login/',views.LoginPage, name='login'),
    path('register/',views.RegisterPage, name='register'),
    path('logout/', views.LogoutUser, name='logout'),
    path('', views.HomePage, name='home'),
    path('my-parcels/', views.ParcelPage, name='my-parcels'),
    path('book-a-parcel/', views.ParcelBookingPage, name='book-a-parcel'),
]
