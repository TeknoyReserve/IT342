from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views.generic import View
from .forms import *
from passlib.hash import pbkdf2_sha256

# Create your views here.

# def get(self, request,a,b): url dispatcher class based views

# check_password = pbkdf2_sha256.hash(password, rounds=20000, salt_size=16)
#             dec_password = pbkdf2_sha256.verify(password, check_password)


class Home(View):
    def get(self, request):
        return render(request,'index.html')

class Signup(View):
    def get(self, request):
        return render(request,'signup.html')

    def post(self, request):
        uform = UserForm(request.POST)

        if uform.is_valid():
            name = request.POST.get("name")
            email = request.POST.get("email")
            contact = request.POST.get("contact")
            address = request.POST.get("address")
            username = request.POST.get("username")
            password = request.POST.get("password")

            enc_password = pbkdf2_sha256.encrypt(password, rounds=12000, salt_size=16)
            tpassword = enc_password

            uform = Users(name=name, email=email, contact=contact, address=address, username=username,
                password=tpassword)

            uform.save()
            print('napindot')
            return redirect('project:home_view')

        else:
            print(uform.errors)
            return HttpResponse('not valid')    
        