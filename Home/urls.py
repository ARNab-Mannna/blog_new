from django.urls import path

from .views import *

urlpatterns = [
    path('',index,name='home'),
    path('about',about,name='about'),
    path('contact',contact,name='contact'),
    path('blog_post',blog_post,name='blogpost'),
    path('scarch',scarch,name='scarch'),
    path('blog_detail/<slug>',blog_detail ,name='blog_detail')
]

