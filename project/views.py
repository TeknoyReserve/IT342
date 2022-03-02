from django.shortcuts import render
from django.views.generic import View

# Create your views here.

# def get(self, request,a,b): url dispatcher class based views
class Home(View):
    def get(self, request):
        return render(request,'index.html')

class Signup(View):
    def get(self, request):
        return render(request,'signup.html')