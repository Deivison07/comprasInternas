# Generated by Django 3.2.5 on 2021-10-12 01:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compras_internas', '0011_alter_oportunidade_imagem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='oportunidade',
            name='imagem',
            field=models.ImageField(blank=True, null=True, upload_to='compras_internas/static'),
        ),
    ]