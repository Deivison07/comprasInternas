from django.forms import ModelForm
from django.contrib.auth.models import User

class User_Form(ModelForm):
    class Meta():
        model = User # indica qual tabela que será colocada no formulario
        fields =['id','username','password'] #os campos que o formulario vai ter, como referencia as colunas da tabela