from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.utils import timezone

from blog.forms import PostCreateForm
from .models import Post


def post_list(request):
    posts = Post.objects.all()
    context = {
        'posts': posts,
    }
    return render(request, 'blog/post_list.html', context = context)


def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    context = {
        'post': post
    }
    return render(request, 'blog/post_detail.html', context)


def post_create(request):
    # 요청이 GET 방식이면 빈 폼을 보여준다.
    if request.method == 'GET':
        form = PostCreateForm()
        context = {
            'form': form
        }
        return render(request, 'blog/post_create.html', context)
    elif request.method == 'POST':
        data = request.POST
        form = PostCreateForm(request.POST)
        post = Post.objects.create(
            title=form['title'],
            text=form['text'],
            author=User.objects.first()
        )
        return redirect('post_detail', pk=post.pk)