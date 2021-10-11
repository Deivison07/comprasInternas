from django.shortcuts import render
from .models import Oportunidade, Profile
from django.contrib.auth.models import User

from django.contrib.auth.decorators import *
from django.contrib.admin.views.decorators import staff_member_required

@login_required

def login(request):
    try:
        user = request.user
        user.profile.pontos
        #user.profile.pontos = 100
        #print(user.is_staff)  -- verifica se é staff o usuario
        #user.profile.pontos = 100
        #user.save()
        #print(user.profile.pontos)
    except:
        prof = Profile()
        prof.user = user
        prof.pontos = 0
        prof.save()

    return render(request,'comprasInternas/index.html')
    
@login_required
@staff_member_required
def list_oportunidades(request):
    dados = {}
    dados['rows'] = portunidades = Oportunidade.objects.all()
    return render(request,'comprasInternas/listagemOportunidades.html',context=dados)


def list_User(request):
    data = {}
    data['rows'] = User.objects.all()
    return render(request, 'comprasInternas/listUsers.html', context=data)



