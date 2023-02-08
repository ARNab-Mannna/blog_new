
from django.contrib.auth.models import User
from django.db import models
from froala_editor.fields import FroalaField
# from django.template.defaultfilters import slugify
from .helpers import *





class blog_model_new1(models.Model):
    title=models.CharField(max_length=1000)
    content=FroalaField()
    user=models.ForeignKey(User ,blank=True,null=True,on_delete=models.CASCADE)
    slug=models.SlugField(max_length=1000,null=True,blank=True)
    image = models.ImageField(upload_to="img_blog",default=" ")
    created_at=models.DateTimeField(auto_now_add=True)
    update_to=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slug_genarate(self.title)
        super(blog_model_new1, self).save(*args, **kwargs)



class Contact(models.Model):
    name=models.CharField(max_length=150)
    email=models.EmailField(max_length=150)
    phone=models.CharField(max_length=12)
    msg= models.TextField(max_length=150)
    date=models.DateField()


    def __str__(self):
        return self.name