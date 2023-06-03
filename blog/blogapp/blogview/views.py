from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Post
from django.contrib import messages
from .forms import PostForm


# Create your views here.

def create_form(request):
    if request.method == 'GET':
        context = {'form': PostForm()}
        return render(request, 'blog/post_form.html', context)
    elif request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'The post has been created successfully.')
            return redirect('posts')
        else:
            messages.error(request, 'Please correct the following errors:')
            return render(request, 'blog/post_form.html', {'form': form})
def home(request):
    posts = Post.objects.all()
    context = {
        'posts':posts,
        'title':"Posts"
    }
    return render(request,'blog/home.html',context)

def about(request):
    messages.error(request, 'Please correct the following errors:')
    return  render(request,'blog/about.html',{'title':"about"})