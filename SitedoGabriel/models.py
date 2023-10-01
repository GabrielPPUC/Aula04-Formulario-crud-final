from django.db import models


# Create your models here.
class hobbies(models.Model):
    OPCOESAMIGOS = [
        ("S", "Sim"),
        ("N", "Nao"),
    ]
    titulo = models.CharField(max_length=50)
    tipo = models.CharField(max_length=50)
    amigos = models.CharField(max_length=1, choices=OPCOESAMIGOS)
    competicao = models.CharField(max_length=20)


class games(models.Model):
    OPCOESCOMPETICAO = [
        ("S", "Sim"),
        ("N", "Nao"),
    ]
    OPCOESESFORCOCOMPUTACIONAL = [
        ("A", "alto"),
        ("M", "médio"),
        ("B", "baixo"),
    ]
    titulo = models.CharField(max_length=50)
    genero = models.CharField(max_length=50)
    competicao = models.CharField(max_length=1, choices=OPCOESCOMPETICAO)
    esforcoComputacional = models.CharField(max_length=1,
                                            choices=OPCOESESFORCOCOMPUTACIONAL)
    frequencia = models.IntegerField()
