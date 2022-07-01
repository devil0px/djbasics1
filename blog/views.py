from django.shortcuts import render
from .models import post
from .forms import PostForm

# Create your views here.
def post_list(request):
    all_posts = post.objects.all()
    context = {'posts':all_posts}
    return render(request,'post/post_list.html',context)


def post_detail(request,id):

    my_post = post.objects.get(id=id)

    return render(request,'post/post_detail.html',{'posts':my_post})



def new_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST ,request.FILES)
        if form.is_valid():
            form.save()
            
    else:
        form = PostForm()

    return render (request ,'post/new_post.html',{'form':form})



def edit_post(request,id):
    post= post.objects.get(id=id)
    if request.method == 'POST':
        form = PostForm(request.POST ,request.FILES,instance=post)
        if form.is_valid():
            form.save()
    else:
        form = PostForm(instance=post)

    return render (request ,'post/new_post.html',{'form':form})