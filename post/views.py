from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import Post

def home(request):
    posts = Post.objects
    return render(request, 'post/home.html', {'posts':posts})

@login_required(login_url="/account/login")
def create(request):
    if request.method == "POST":
        if request.POST['tag'] and request.FILES['image']:
            post = Post()
            post.tag = request.POST['tag']
            post.image = request.FILES['image']
            post.post_date = timezone.datetime.now()
            post.user = request.user
            post.save()
            return redirect('home')
        else:
            return render(request, 'post/create.html',{'error':'Please update all things'})
    else:
        return render(request, 'post/create.html')

def details(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'post/detail.html', {'post':post})

@login_required(login_url="/account/login")
def like_post(request, post_id):
    if request.method == "POST":
        post = get_object_or_404(Post, pk=post_id)
        post.likes += 1;
        post.save()
        print("done done done")
        return redirect('/'+str(post_id))

@login_required(login_url="/account/login")
def dislike_post(request, post_id):
    if request.method == "POST":
        post = get_object_or_404(Post, pk=post_id)
        post.dislikes += 1;
        post.save()
        print("whats happening")
        return redirect('/'+str(post_id))
