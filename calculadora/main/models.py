from django.db import models

class Calculadora(models.Model):
    valor1 = models.FloatField()
    valor2 = models.FloatField()
    operacao = models.CharField(max_length=1)
    resultado = models.FloatField()