# Generated by Django 3.2.5 on 2021-10-08 03:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Administrador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('data', models.DateField(auto_now_add=True)),
                ('senha', models.CharField(max_length=10)),
            ],
            options={
                'verbose_name_plural': 'Administradores',
            },
        ),
        migrations.CreateModel(
            name='Colaborador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('data', models.DateField(auto_now_add=True)),
                ('pontuacao', models.DecimalField(decimal_places=2, max_digits=7)),
                ('senha', models.CharField(max_length=10)),
            ],
            options={
                'verbose_name_plural': 'Colaboradores',
            },
        ),
        migrations.CreateModel(
            name='Oportunidade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('descricao', models.TextField()),
                ('data', models.DateField(auto_now_add=True)),
                ('pontuacao', models.DecimalField(decimal_places=2, max_digits=7)),
                ('imagem', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'Oportunidades',
            },
        ),
        migrations.CreateModel(
            name='Historico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('colaborador', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='compras_internas.colaborador')),
                ('oportunidade', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='compras_internas.oportunidade')),
            ],
        ),
    ]
