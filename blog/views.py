from django.shortcuts import render
from django.utils import timezone
from .models import Post

def post_list(request):
    return render(request, 'blog/index.html', {})

def google_rozklad(request):
    return render(request, 'blog/rozklad.html', {})

def predmets(request):
    posts = Post.objects.filter(published_date__lte=timezone.now())
    return render(request, 'blog/prdmets.html', {'posts': posts})

def news(request):
    return render(request, 'blog/news.html', {})

def home(request):
    return render(request, 'blog/base.html', {})