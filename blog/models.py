from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class category(models.Model):
    category = models.CharField(max_length=255)
    description = models.CharField(max_length=255,default="")
    def __str__(self):
        return self.category

class blog(models.Model):
    category = models.ForeignKey(category, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User,on_delete=models.CASCADE,)
    date = models.DateField(auto_now_add=True)
    description = models.TextField()
    image = models.ImageField(upload_to="blog_images",null=True,blank=True)
    