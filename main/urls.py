
from django.contrib import admin
from django.urls import path,include

from compras_internas.views import login,administrador,add_oportunidades,deleteColab,deleteOport


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/',include('django.contrib.auth.urls')),
    path('',login),
    path('adm/',administrador,name='url_admistrador'),
    path('delete/colab/<int:pk>',deleteColab,name='url_admistrador'),
    path('delete/oport/<int:pk>',deleteOport,name='url_admistrador'),
    path('addOportunidades/',add_oportunidades,name='url_add_oportunidades'),
    path('addOportunidades/<int:pk>',add_oportunidades,name='url_add_item'),
]



