from django.shortcuts import render
from django.http import HttpResponse
import datetime
from .models import Transacao

# Create your views here.
def home(request):
    data = {}
    data['transacoes'] = ['t1', 't2', 't3']
    data['now'] = datetime.datetime.now()
    # html = "<html><body>It is now %s.</body></html>" % now

    return render(request, 'contas/home.html', data)  # HttpResponse(html)

def listagem(request):
    data = {}
    data['transacoes'] = Transacao.objects.all()  # objects é um Manager
    return render(request, 'contas/listagem.html', data)

# Manager :: uma classe que o Django implementa para todos os models, trazendo operacoes de BD:
# all(), filter(), last(), first().