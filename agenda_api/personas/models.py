from django.db import models

# Create your models here
class Persona(models.Model):
    documento = models.BigIntegerField(unique=True)
    nombre= models.CharField(max_length=25)
    apellido= models.CharField(max_length=25)
    correo = models.EmailField()
    pais= models.CharField(max_length=25)
    ciudad = models.CharField(max_length=50)
    
    def __str__(self):
        return f"{self.nombre}{self.apellido}"
