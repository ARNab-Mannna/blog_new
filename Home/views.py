from django.shortcuts import render, redirect
# from django.contrib.auth.models import User
from datetime import datetime
# from Home.models import *
from .form_blog import *
from django.contrib import messages
from accounts import views
from django.core.paginator import Paginator






def index(request):
    page_obj= blog_model_new1.objects.all().order_by('id')
    
    pentor= Paginator(page_obj,9)
    page_num = request.GET.get('page')
    # try:
    blogs = pentor.get_page(page_num)
    # print(page_obj)
    # print('*******')
    # print(pentor)
    # print('*******')
    # print( page_num)
    # print('*******')
    # print(blogs)
    # except EmptyPage:
    # page = page_num.page(1)
    

    context={'blogs':blogs}
    return render (request,'index.html',context)
    # return render(request, 'index.html')

def blog_detail(request ,slug):
    context= {}
    try:
        slug_obj = blog_model_new1.objects.filter(slug=slug).first()
        context= {'slug_obj': slug_obj}
    except Exception as e:
        print (e)
    return render(request, 'blog_detail.html',context)

def about(request):
    return render(request, 'blog_from.html')

def scarch(request):
    query=request.GET['query']
    all_blog = blog_model_new1.objects.filter(title__icontains=query)
    context_s={'all_blog':all_blog}

    return render(request, 'scarch.html',context_s)

'''*****************************************************************
********************************************************************'''

def contact(request):
   

    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        msg = request.POST.get('message')
        date = request.POST.get('date')
        if len(name)<4 or len(email)<4 or len(phone)<10 or len(msg)<5:
            messages.error(request, 'Please Fill The Form Currectlly !')
        else:
            contact = Contact(name=name, email=email, phone=phone,msg=msg, date=datetime.today())
            contact.save()
            messages.success(request, 'Contact form sussesfully submited.')
    return render(request, 'contact.html')

from Home.models import blog_model_new1

def blog_post(request):
    context={'form':Blogform}
    try:
        if request.method == 'POST':
            title = request.POST.get('title')
            form = Blogform(request.POST)
            image = request.FILES['image']
            user=request.user      
            print (request.user)


            if form. is_valid():
                content=form.cleaned_data['content']
                blog_model_new1.objects.create(user = user ,title = title ,content = content, image = image)
                messages.success(request, 'Your Blog sussesfully submited.')
            return redirect ('/blog_post')
           
        # else: image= request.FILES[image]s
    except Exception as e:
        
        print(e)

    return render(request, 'blog_from.html',context)


   
#git checkout -b port_branch
#git remote set-url https://ARNab-Mannna@github.com/ARNab-Mannna/portfoio.git
# https://github.com/ARNab-Mannna/Blog_Project.git