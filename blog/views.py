from django.shortcuts import render, redirect
from .models import Post
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm

def index(request):
    posts = Post.objects.all()
    return render(request, 'home.html',{'posts':posts})

def listaPosts(request):
    search = request.GET.get('search')
    if search:
        lista = Post.objects.filter(titulo__icontains=search)
        return render(request, 'listaPosts.html',{'lista':lista})
    else:
        lista = Post.objects.order_by('-id').all()
        return render(request, 'listaPosts.html',{'lista':lista})
    
def detalhePost(request, id):
    detalhe = Post.objects.get(id=id)
    return render(request, 'detalhePost.html',{'detalhe':detalhe})

def login_view(request):
    if request.method=='POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login') 
