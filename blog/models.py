from pyexpat import model
from tabnanny import verbose
from turtle import title
from unittest import mock
from django.db import models
from django.forms import ImageField
from django.utils import timezone

class Category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self) :
        return self.name

    class Meta:
        verbose_name = "Category"
        verbose_name_plural="categories"
        





# Create your models here.
class post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=10000)
    #publish_date = models.DateField(default=timezone.now)
    #update_date = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='posts/')
    category = models.ForeignKey(Category,on_delete=models.CASCADE)

    def __str__(self) :
        return self.title

    class Meta:
       verbose_name= "my posts"
       #ٍordering = ['-publish_date']
