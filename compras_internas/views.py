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
    
@login_required
@staff_member_required
def list_oportunidades(request):
    dados = {}
    dados['rows'] = portunidades = Oportunidade.objects.all()
    return render(request,'comprasInternas/listagemOportunidades.html',context=dados)


def list_User():
    data = {}
    data['rows'] = User.objects.all()
    return data
    #return render(request, 'comprasInternas/listUsers.html', context=data)


@login_required
@staff_member_required
def administrador(request):
    list = list_User()
    return render(request,'comprasInternas/adiministrador.html',context=list)

def modificarUser(request,pk):
    data = {}
    user = User.objects.get(pk=pk)





