from django.utils.text import slugify
import string
import random
 




def genarate_random_string(N):
    res = ''.join(random.choices(string.ascii_uppercase + string.digits, k=N))
    return res




def slug_genarate(text):
    new_slug=slugify(text)
    from .models import blog_model_new1
    if blog_model_new1.objects.filter(slug =new_slug).exists():
        return slug_genarate(text + genarate_random_string(5) )
          
    return new_slug
