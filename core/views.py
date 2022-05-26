from django.shortcuts import render, redirect
from core.models import Evento


# Create your views here.
#def index(requests):
#    return redirect('/agenda/')

def lista_eventos(requests):
    #usuario = requests.user
    evento = Evento.objects.all()
    dados = {'eventos': evento}
    return render(requests, 'agenda.html', dados)
