from django.urls import path
from .views import post_list , post_detail , new_post ,edit_post

app_name = 'blog'
urlpatterns = [
   
    path('' ,post_list ,name='post_lest'),
    path('new' ,new_post ,name ='new_post'),   
    path('<int:id>' , post_detail ,name='post_detail'),
    path('<int:id>/edit',edit_post,name='edit_post')
]