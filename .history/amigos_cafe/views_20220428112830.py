from .models import Profile
from amigos_cafe.models import Booking
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from .models import *
import uuid
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from datetime import datetime

# Create your views here.
@login_required(login_url='/')
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def blog(request):
    return render(request, 'blog.html')

def booking(request):
    if request.method=="POST":
        name= request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        date = request.POST.get("date")
        time = request.POST.get("time")
        members = request.POST.get("grp")
        # booking = Booking(name =name, email=email, phone= phone)
        booking = Booking(name =name, email=email, phone= phone, date=date, time=time, members= members)
        booking.save()
        print(members)
        messages.success(request, 'Your Table is booked successfully. You will receive a message on your registered mobile number', phone)
    return render(request, 'booking.html')

def contact(request):
    return render(request, 'contact.html')

def feature(request):
    return render(request, 'feature.html')

def index(request):
    return render(request, 'index.html')

def menu(request):
    return render(request, 'menu.html')

    
def userlogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user_obj = User.objects.filter(username = username).first()
        if user_obj is None:
            messages.success(request, 'User not found.')
            return redirect('/login')
        
        
        # profile_obj = Profile.objects.filter(user = user_obj ).first()

        # if not profile_obj.is_verified:
        #     messages.success(request, 'Profile is not verified check your mail.')
        #     return redirect('/accounts/login')

        user = authenticate(username = username , password = password)
        if user is None:
            messages.success(request, 'Wrong password.')
            return redirect('/login')
        
        login(request , user)
        return redirect('/')

    return render(request , 'login.html')

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        print(password)

        try:
            if User.objects.filter(username = username).first():
                messages.success(request, 'Username is taken.')
                return redirect('/register')

            if User.objects.filter(email = email).first():
                messages.success(request, 'Email is taken.')
                return redirect('/register')
            
            user_obj = User(username = username , email = email)
            user_obj.set_password(password)
            user_obj.save()
            auth_token = str(uuid.uuid4())
            profile_obj = Profile.objects.create(user = user_obj , auth_token = auth_token)
            profile_obj.save()
            # send_mail_after_registration(email , auth_token)
            messages.success(request, 'User Registered successfully.')
            return redirect('/')

        except Exception as e:
            print(e)


    return render(request , 'register.html')
    
def signout(request):
    logout(request)
    return redirect("/login")
    
# def token(request):
    # return render(request, 'token.html')

# def send_mail_after_registration(email , token):
#     subject = 'Your account needs to be verified'
#     message = f'Hi paste the link to verify your account http://127.0.0.1:8000/verify/{token}'
#     email_from = settings.EMAIL_HOST_USER
#     recipient_list = [email]
#     send_mail(subject, message , email_from ,recipient_list )