from django.urls import path
from .views import *

urlpatterns = [
    path('',Home,name='home'),
    path('about/',About,name='about'),
    path('service/',Service,name='service'),
]