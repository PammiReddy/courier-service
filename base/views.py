from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import Parcel
from .forms import ParcelForm,CustomUserCreationForm
from django.contrib.auth.decorators import login_required


# Create your views here.

def LoginPage(request):
  if request.user.is_authenticated:
    return redirect('home')
  
  if request.method == 'POST':
    email = request.POST.get('email').lower()
    password = request.POST.get('password')
    
    try:
      user = User.objects.get(email=email)
    except User.DoesNotExist:
      messages.error(request, 'User does not exist')
      return redirect('login')
    
    user = authenticate(request, username=user.username, password=password)
    if user is not None:
      login(request, user)
      return redirect('home')
    else:
      messages.error(request, 'Email or password is incorrect')

  return render(request, 'base/login.html')

def RegisterPage(request):
    if request.user.is_authenticated:
      return redirect('home')

    if request.method == 'POST':
      form = CustomUserCreationForm(request.POST)
      if form.is_valid():
        user = form.save(commit=False)
        user.username = user.username.lower()
        user.save()
        login(request, user)
        messages.success(request, "Registration successful.")
        return redirect('home')
      else:
        messages.error(request, "Unsuccessful registration. Invalid information.")
    else:
      form = CustomUserCreationForm()

    return render(request, "base/register.html", {"form": form})

def LogoutUser(request):
  logout(request)
  return redirect('home')

@login_required(login_url='login')
def HomePage(request):
   my_bookings = Parcel.objects.all()
   context = {
      'my_bookings': my_bookings
   }
   return render(request, 'base/home.html',context)

@login_required(login_url='login')
def ParcelPage(request):
   my_bookings = Parcel.objects.filter( host = request.user)
   context = {
      'my_bookings': my_bookings
   }
   return render(request, 'base/booking-list.html',context)

@login_required(login_url='login')
def ParcelBookingPage(request):
  form = ParcelForm() 
  if request.method == 'POST':
    form = ParcelForm(request.POST)
    if form.is_valid():
      parcel = form.save(commit=False)
      parcel.host = request.user
      parcel.save()
      return redirect('my-parcels')
  context ={'form':form}
  return render(request,'base/book-a-parcel.html',context)

