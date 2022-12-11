from multiprocessing import context
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout



from .forms import FormularioRegistro, FormularioLogin


# Create your views here.
def index(request):
   
    return render(request, "index.html")


def loginUser(request):
    
    titulo = 'Login'
    form = FormularioLogin(request.POST or None)

    if form.is_valid():
    
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        usuario = authenticate(username = username, password = password)
        login(request, usuario)
        return redirect('index')
    
    context = {
        'form': form,
        'titulo': titulo,
    }

    return render(request, 'usr/login.html', context)


def registro(request):

    head = 'Crear una cuenta'
    if request.method == 'POST':
        form = FormularioRegistro(request.POST)

        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = FormularioRegistro()
    context = {
        'form': form,
        'head': head
    }

    return render(request, 'usr/registro.html', context)





def plastas(request):
    return render(request, "libro/plastas.html")

def abrazoArbol(request):
    return render(request, "libro/abrazoArbol.html")

def ninasRebeldes(request):
    return render(request, "libro/ninasRebeldes.html")

def buscaLibros(request):
    return render(request, "libro/buscaLibros.html")