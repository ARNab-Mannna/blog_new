from django.urls import path
from .views import *


urlpatterns = [
    
        
        path('' , Register,name='register'),
        path('register' , Register,name='register'),
        path('login', login,name='login'),
        path('logout', logout,name='logout')
]