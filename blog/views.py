from pyexpat import model
from django.shortcuts import redirect, render
from .models import post
from .forms import PostForm

# Create your views here.
def post_list(request):
    all_posts = post.objects.all()
    context = {'posts':all_posts}
    return render(request,'blog/post_list.html',context)

def post_detail(request,id):

    my_post = post.objects.get(id=id)

    return render(request,'blog/post_detail.html',{'post':my_post})

def new_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST ,request.FILES)
        if form.is_valid():
            form.save()
            
    else:
        form = PostForm()

    return render (request ,'blog/new_post.html',{'form':form})

def edit_post(request,id):
    Post = post.objects.get(id=id)
    if request.method == 'POST':
        form = PostForm(request.POST ,request.FILES,instance=Post)
        if form.is_valid():
            form.save()
    else:
        form = PostForm(instance=Post)

    return render (request ,'post/new_post.html',{'form':form})

def delete_post(request,id):

    Post = post.objects.get(id=id)
    Post.delete()
    return redirect('/blog')
# Create your views class 
from django.views.generic import ListView,DetailView,DeleteView

class PostList(ListView):
    model=post

class PostDetail(DetailView):
    model=post

class DeletePost(DeleteView):
    model=post
    success_url = '/blog/cbv'