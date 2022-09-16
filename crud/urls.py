from django.contrib import admin  
from django.urls import path, include
#from credential import views as user_view
#from django.contrib.auth import views as auth
from employee import views 
#from credential import views 
urlpatterns = [  
    path('',include('users.urls')),           
    path('', views.index, name='home'),          
    path('admin/', admin.site.urls),  
    
    path('emp', views.emp),  
    path('show',views.show),  
    path('edit/<int:id>', views.edit),  
    path('update/<int:id>', views.update),  
    path('delete/<int:id>', views.destroy),  
] 