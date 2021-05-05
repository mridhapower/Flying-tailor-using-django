from django.urls import path,include

from . import views

urlpatterns = [
    path('tailors/',include('tailors.urls'),name='tailors'),
    path('', views.login, name="login"),
    

]
