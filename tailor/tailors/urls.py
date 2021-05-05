from django.urls import path,include

from . import views

urlpatterns = [
        path('tailor', views.tailor, name="tailor"),
        path('',views.location,name="locations"),

]