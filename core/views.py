from django.shortcuts import render, HttpResponse

# Create your views here.

def hello(request, nome, idade):
    return HttpResponse(f'<h2>hello {nome} de {idade} anos</h2>')

def soma(request, n1, n2):
    return HttpResponse(f'<h1>A soma de {n1} e {n2} é {n1+n2}</h1>')

def subtracao(request, n1, n2):
    return HttpResponse(f'<h1>A subtração de {n1} e {n2} é {n1-n2}</h1>')

def mult(request, n1, n2):
    return HttpResponse(f'<h1>A multiplicação de {n1} e {n2} é {n1*n2}</h1>')

def divisao(request, n1, n2):
    if n2 != 0:
        return HttpResponse(f'<h1>A divisão inteira de {n1} e {n2} é {n1/n2}</h1>')
    else:
        return HttpResponse('<h1> Error, não existe divisão por 0 </h1>')


