from django.shortcuts import render,redirect
from .models import Location, Shop

def location(request):
    #print(username=request)
    locations = Location.objects.all()
    name=request.session['name']
    #loc=request.POST.get('loc')
    if (request.method == 'POST' and request.POST.get('loc')!=None):
        loc=request.POST.get('loc')
        print(loc)
        #id=Shop.objects.get(loc_id=loc)
        shops=Shop.objects.filter(loc_id=loc)
        locationName=list(Location.objects.filter(id=loc).values_list('loc', flat=True))
        print(locationName[0])
        #print(shops)
        return render(request,'tailors.html',{'name':name,'shops':shops,'loc':loc,'locationName':locationName[0]})
    else:
        button=request.POST.get('button')
        print(button)
        return render(request,'locations.html',{'locations':locations,'name':name})
        #return redirect('location.html')
    
    

def tailor(request):
    return render(request,'locations.html')
    
