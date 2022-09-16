
from unicodedata import name
from django.urls import path,include
from . import views

urlpatterns = [
  
  path('',views.Index,name='index'),
  path('login/',views.Login,name='login'),
  path('register/',views.Register,name='register'),
  
]
