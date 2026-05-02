import json

from django.shortcuts import render
from django.http import HttpResponse, Http404
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent


def home(request):
    return render(request, 'main/home.html')


def blog(request):
    file_path = BASE_DIR / 'data' / 'posts.json'

    with open(file_path, 'r') as f:
        posts = json.load(f)

    return render(request, 'main/blog.html', {'posts': posts})


def post_detail(request, post_id: int):
    file_path = BASE_DIR / 'data' / 'posts.json'

    with open(file_path, 'r') as f:
        posts = json.load(f)

    for p in posts:
        if p['id'] == post_id:
            return render(request, 'main/post_detail.html', {'post': p})
        
    raise Http404("Post topilmadi")