# Generated by Django 3.2.5 on 2021-10-11 19:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('compras_internas', '0007_rename_pontualcao_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registro',
            name='colaborador',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='registro',
            name='oportunidade',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='compras_internas.oportunidade'),
        ),
    ]
