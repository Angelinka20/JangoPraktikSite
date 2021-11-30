from django.shortcuts import render
from django.utils import timezone
from .models import Post, News
from django.shortcuts import render, get_object_or_404

def post_list(request):
    return render(request, 'blog/index.html', {})

def google_rozklad(request):
    return render(request, 'blog/rozklad.html', {})

def predmets(request):
    posts = Post.objects.filter()
    return render(request, 'blog/prdmets.html', {'posts': posts})

def news(request):
    news = News.objects.filter(published_date__lte=timezone.now())
    return render(request, 'blog/news.html', {'news': news})

def home(request):
    return render(request, 'blog/base.html', {})

def marks(request):
    posts = Post.objects.filter()
    return render(request, 'blog/marks.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/s.html', {'post': post})