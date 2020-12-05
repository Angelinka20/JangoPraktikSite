from django.shortcuts import render

def post_list(request):
    return render(request, 'blog/index.html', {})

def google_rozklad(request):
    return render(request, 'blog/rozklad.html', {})
