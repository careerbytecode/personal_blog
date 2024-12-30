from django.shortcuts import render
from .models import Post
from .forms import PostForm
from django.shortcuts import render, get_object_or_404, redirect


def home(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'home.html', {'posts': posts})

from django.shortcuts import redirect

def add_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = PostForm()
    return render(request, 'add_post.html', {'form': form})

def edit_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirect to the list of posts
    else:
        form = PostForm(instance=post)

    return render(request, 'edit_post.html', {'form': form})

def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    post.delete()  # Delete the post
    return redirect('home')  # Redirect to the list of posts

