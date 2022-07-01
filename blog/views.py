from django.shortcuts import render
from .models import post

# Create your views here.
def post_list(request):
    all_posts = post.objects.all()
    context = {'posts':all_posts}
    return render(request,'post/post_list.html',context)


def post_detail(request,id):

    my_post = post.objects.get(id=id)

    return render(request,'post/post_detail.html',{'posts':my_post})