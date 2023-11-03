from django.shortcuts import render
from .models import Post

def index(request):
    posts = Post.objects.all()
    return render(request, 'home.html',{'posts':posts})

def listaPosts(request):
    lista = Post.objects.all()
    return render(request, 'listaPosts.html',{'lista':lista})
    


def detalhePost(request):
    return render(request, 'detalhePost.html')
