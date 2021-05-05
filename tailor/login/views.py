from django.contrib import messages
from django.shortcuts import render,redirect

from .models import Customer


# Create your views here.
def login(request):
    if request.method == 'POST' and request.POST.get('type')!="" and request.POST.get('checklog')!="" and request.POST.get('name')!="" and request.POST.get('password')!="":
        name = request.POST.get('name')
        password = request.POST.get('password')
        checklog =  request.POST.get('checklog')
        print(checklog)
        if checklog=='Customer' and Customer.objects.filter(name=name,password=password).exists():            
            """ messages.success("boo") """
            return redirect('locations')
        else:
            return render(request,'login.html')
    else:
        return render(request,'login.html')
