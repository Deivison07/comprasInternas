# Generated by Django 3.2.5 on 2021-10-08 16:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('compras_internas', '0003_alter_oportunidade_imagem'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Administrador',
        ),
        migrations.RemoveField(
            model_name='historico',
            name='colaborador',
        ),
        migrations.RemoveField(
            model_name='historico',
            name='oportunidade',
        ),
        migrations.DeleteModel(
            name='Colaborador',
        ),
        migrations.DeleteModel(
            name='Historico',
        ),
    ]