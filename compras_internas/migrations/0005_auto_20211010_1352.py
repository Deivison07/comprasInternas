# Generated by Django 3.2.5 on 2021-10-10 16:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('compras_internas', '0004_auto_20211008_1306'),
    ]

    operations = [
        migrations.AlterField(
            model_name='oportunidade',
            name='imagem',
            field=models.ImageField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='oportunidade',
            name='pontuacao',
            field=models.IntegerField(),
        ),
        migrations.CreateModel(
            name='Pontualcao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pontos', models.IntegerField()),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
