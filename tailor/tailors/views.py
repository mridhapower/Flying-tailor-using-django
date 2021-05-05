from django.shortcuts import render,redirect
from .models import Location, Shop

def location(request):
    locations = Location.objects.all()
    if (request.method == 'POST' and request.POST.get('loc')!=''):
        loc=request.POST.get('loc')
        #id=Shop.objects.get(loc_id=loc)
        shops=Shop.objects.filter(loc_id=loc)
        #print(shops)
        return render(request,'tailors.html',{'shops':shops})
    else:
        
        return render(request,'locations.html',{'locations':locations})
        #return redirect('location.html')
    
    

def tailor(request):
    return redirect('location.html')
    
