from django.shortcuts import render, HttpResponse

# Create your views here.

def index(request):
    return render(request, 'piemonte/index.html')

def emprestimos(request):
    return render(request, 'piemonte/emprestimos.html')

def contato(request):
    return render(request, 'piemonte/contato.html')

def consorcios(request):
    return render(request, 'piemonte/consorcios.html')

def produtos(request):
    return render(request, 'piemonte/produtos.html')