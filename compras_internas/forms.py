from django.contrib.auth.models import User
from django.forms import ModelForm

class Transacao_Form(ModelForm):
    class Meta():
        model = User
        fields =['id','descricao','valor','categoria']
