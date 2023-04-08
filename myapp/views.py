from django.shortcuts import render
from .models import Post

def index(request):
    posts = Post.objects.all()
    index_content = {
        "posts" : posts
    }
    return render(request, "index.html", index_content)

def post(request, pstr):
    posts = Post.objects.get(id=pstr)
    post_content = {
        "posts" : posts
    }
    return render(request, "posts.html", post_content)