
from django.contrib import admin
from django.urls import path,include
from compras_internas.views import login,list_oportunidades,list_User


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/',include('django.contrib.auth.urls')),
    path('',login),
    path('listar/',list_oportunidades),
    path('users/',list_User),
]