from django.shortcuts import render,redirect
from .models import Oportunidade, Profile, Registro
from django.contrib.auth.models import User

from django.contrib.auth.decorators import *
from django.contrib.admin.views.decorators import staff_member_required

@login_required

def login(request):
    try:
        user = request.user
        user.profile.pontos

    except:
        prof = Profile()
        prof.user = user
        prof.pontos = 0
        prof.save()


    if user.is_staff:
        return redirect('url_admistrador')

    data = {}
    reg = Registro.objects.filter(colaborador=user)
    data['reg'] = reg

    return render(request,'comprasInternas/index.html',context=data)
    

def list_oportunidades():
    dados = {}
    dados['rows'] = Oportunidade.objects.all()
    return dados

def list_User():
    data = {}
    data['rows'] = User.objects.all()
    return data


@login_required
@staff_member_required
def administrador(request):
    data = {}
    data['usuarios'] = list_User()
    data['oportunidades']= list_oportunidades()

    return render(request,'comprasInternas/adiministrador.html',context=data)

@login_required
def add_oportunidades(request,pk=None):
    data = {}
    if pk != None:
        user = request.user
        item = Oportunidade.objects.get(pk=pk)

        if user.profile.pontos >= item.pontuacao:
            user.profile.pontos = int(user.profile.pontos) - int(item.pontuacao)

            user.profile.save()
            reg = Registro()
            reg.colaborador = user
            reg.oportunidade = item
            reg.save()
            data['mensagem'] = "Adicionado com Sucesso"
        else:
            data['mensagem'] = "Infelizmente você não tem pontuação"



    data['oportunidades'] = list_oportunidades()
    return render(request, 'comprasInternas/addOportunidades.html', context=data)






