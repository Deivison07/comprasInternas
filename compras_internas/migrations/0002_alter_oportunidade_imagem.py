# Generated by Django 3.2.5 on 2021-10-08 03:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compras_internas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='oportunidade',
            name='imagem',
            field=models.TextField(null=True),
        ),
    ]
