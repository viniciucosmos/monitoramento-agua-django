from django.db import models

class Leituras(models.Model):
    temperatura = models.IntegerField()
    ph = models.IntegerField()
    tds = models.IntegerField()
    data_hora = models.DateTimeField(auto_now_add=True)

def __str__(self):
    return f"{self.temperatura} C | pH: {self.ph} | TDS: {self.tds} | Horario: {self.data_hora}"

