# Generated by Django 3.2.13 on 2023-09-19 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='games',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=50)),
                ('genero', models.CharField(max_length=50)),
                ('competicao', models.CharField(choices=[('S', 'Sim'), ('N', 'Nao')], max_length=1)),
                ('esforcoComputacional', models.CharField(choices=[('A', 'alto'), ('M', 'médio'), ('B', 'baixo')], max_length=1)),
                ('frequencia', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='hobbies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=50)),
                ('tipo', models.CharField(max_length=50)),
                ('amigos', models.CharField(choices=[('S', 'Sim'), ('N', 'Nao')], max_length=1)),
                ('competicao', models.CharField(max_length=20)),
            ],
        ),
    ]
