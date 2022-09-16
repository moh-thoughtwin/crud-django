from django.urls import path, include

from . import views

urlpatterns = [
        
        path("<slug:slug>", views.show.as_view(), name="emp_detail"),  # new
        path('', include('employee.urls')),
        path('', views.emp, name='emp'),
        
    ]