from django.shortcuts import render

def post_list(request):
    n = "OLEG"
    return render(request, 'blog/index.html', context={'name':n})