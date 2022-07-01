from csv import list_dialects
from pyexpat import model
from django.contrib import admin

# Register your models here.
from  .models import post ,Category

class postAdmin(admin.ModelAdmin):
    list_dialects=['id','title','category']
    search_fields= ['title','content']
    date_hierarchy ='publish_date'



admin.site.register(post,postAdmin)
admin.site.register(Category)


