from django.db import models


class Direccion(models.Model):
    pais = models.CharField(max_length=100)
    provincia = models.CharField(max_length=100)
    calle = models.CharField(max_length=100)
    numero = models.PositiveIntegerField()
    detpo = models.CharField(max_length=100, blank=True)    
    detalle = models.CharField(max_length=300, blank=True)
    mail = models.EmailField()

    def __str__(self):
        return self.pais + ' ' + self.provincia + ' ' + self.calle + ' ' + str(self.numero)


class Persona(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=150)
    dni = models.CharField(max_length=20)
    mail = models.EmailField(blank=True)
    direccion = models.ForeignKey(
        Direccion,
        on_delete = models.CASCADE
    )

    def __str__(self):
        return self.apellido + ' ' + self.nombre + ' ' + self.dni 



