from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from lagun_ezkutua.models import *
import random
from django.core.mail import send_mail
# Create your views here.

def index2(request):
    lag = KuadrillaForm()
    return HttpResponse("Lagun ezkutua")

def index(request):
    form = KuadrillaForm(request.POST or None)
    if form.is_valid():
        instances = form.save()
        return HttpResponseRedirect(str(instances.id)+'/izenak/')
    return render(request, 'lagun_ezkutua/sarrera.html', {'form':form})

def epostak_bidali(hiztegia):
    for izena in hiztegia:
        
        send_mail(
            'Lagun ezkutuko laguna',
            'Kaixo '+izena+', aurtengo lagun ezkutuan '+hiztegia[izena][1]+' lagunari egin behar diozu oparia. Ondo izan.',
            'lagunezkutua.python@gmail.com',
            [hiztegia[izena][0]],
            fail_silently=False,
)

def zozketa(lagunak):
    random.shuffle(lagunak)
    zozketa = {}
    for i in range(0,len(lagunak)): 
        zozketa[lagunak[i]]=lagunak[(i+1)%len(lagunak)]
    return zozketa

def izenak(request,kuadrilla_id):

    k = Kuadrilla.objects.get(id=kuadrilla_id)
    form = LagunaForm(request.POST or None,extra=k.lagun_kopurua)
    if form.is_valid():
        lagunak = []
        hiztegia = {}
        for (laguna,eposta) in form.extra_lagunak():
            lagunak.append(laguna)
        zoz = zozketa(lagunak)
        print('lagunak',lagunak,zoz)
        for (laguna, eposta) in form.extra_lagunak():
            print(laguna,eposta)
            l = Laguna(kuadri=k,izena=laguna,eposta=eposta,lagun_ezk=zoz[laguna])
            l.save()
            hiztegia[laguna] = (eposta,zoz[laguna])
        epostak_bidali(hiztegia)
        return HttpResponseRedirect('/'+str(kuadrilla_id)+'/emaitza/')
    return render(request, 'lagun_ezkutua/izenak.html', {'form':form})


def emaitza(request,kuadrilla_id):
    
    #return HttpResponse("Zozketaren emaitzak")
    k = Kuadrilla.objects.get(id=kuadrilla_id)
    return render(request,'lagun_ezkutua/emaitza.html',{'kuadrilla':k})
