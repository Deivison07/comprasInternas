from django.db import models
from django.contrib.auth.models import User

class Oportunidade(models.Model):
    nome =  models.CharField(max_length = 100)
    descricao = models.TextField()
    data = models.DateField(auto_now_add=True)
    pontuacao = models.IntegerField()
    imagem = models.ImageField(upload_to='compras_internas/static/',blank=True, null=True)

    def __str__(self):
        return self.nome 
    
    class Meta:
        verbose_name_plural = 'Oportunidades'

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE, null=True)
    pontos = models.IntegerField()

    def __str__(self):
        return str(self.user)

class Registro(models.Model):
    colaborador = models.ForeignKey(User,on_delete=models.CASCADE)
    oportunidade = models.ForeignKey(Oportunidade,on_delete=models.CASCADE)
    


