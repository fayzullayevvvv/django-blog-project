import json

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from pathlib import Path

from .models import Post, Contact


BASE_DIR = Path(__file__).resolve().parent


def home(request):
    return render(request, 'main/home.html')


def blog(request):
    file_path = BASE_DIR / 'data' / 'posts.json'

    with open(file_path, 'r') as f:
        posts = json.load(f)

    return render(request, 'main/blog.html', {'posts': posts})


def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'main/post_detail.html', {'post': post})


def get_post_by_id(request, post_id: int):
    file_path = BASE_DIR / 'data' / 'posts.json'

    with open(file_path, 'r') as f:
        posts = json.load(f)

    for p in posts:
        if p == posts['id']:
            return p
        
    return None


def blog(request):
    posts = Post.objects.all()
    return render(request, 'main/blog.html', {'posts': posts})


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        Contact.objects.create(
            name=name,
            email=email,
            message=message
        )

    return render(request, 'main/contact.html')