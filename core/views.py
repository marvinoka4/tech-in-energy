from django.http import HttpResponse
from django.shortcuts import render

from blog.models import Post


# Create your views here.
def home(request):
    return render(request, 'core/index.html')


def about(request):
    return render(request, 'core/about.html')


def data(request):
    return render(request, 'core/data.html')


def blog(request):
    posts = Post.objects.filter(status=Post.ACTIVE)
    return render(request, 'core/blog.html', {'posts': posts})


def robots_txt(request):
    text = [
        "User-Agent: *",
        "Disallow: /admin/",
    ]
    return HttpResponse("\n".join(text), content_type="text/plain")
