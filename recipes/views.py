from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'recipes/home.html', context={
        'name': 'Valney Filho'
    })


def contato(request):
    return HttpResponse('contato')


def sobre(request):
    return HttpResponse('sobre')
