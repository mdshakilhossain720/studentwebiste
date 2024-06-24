from django.shortcuts import render

# Create your views here.

def base(request):
    return render(request,'common_code/index.html')

def home(request):
    return render(request,'home/home.html')

def loginuser(request):
    return render(request,'login/login.html')

def customeruser(request):
    return render(request,'login/customerregistration.html')

def passwordchange(request):
    return render(request,'login/changepassword.html')

def profile(request):
    return render(request,'login/profile.html')


