from django.db import models
from django.core.validators import URLValidator
from datetime import datetime

# Create your models here.
class grupo(models.Model):
    nombre = models.CharField(max_length=50, verbose_name='Area Encargada')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = ('Area-Grupo')
        verbose_name_plural = ('AREAS-Grupos')
        ordering = ['nombre']
    def __str__(self):
        return self.nombre

tipfile = [
    ["MP4", "Video"],
    ["JPG", "Foto-Imagen"],
    ["MP3", "Musica-Sonido"],
    ["PDF", "Documento Pdf"],
]

class inicio(models.Model):
    titulo=models.CharField(max_length=50,verbose_name='Nombre' )
    grupo = models.ForeignKey(grupo, on_delete=models.CASCADE, verbose_name='Area Encargada')
    contenido = models.TextField()
    archivo = models.FileField(upload_to='inicio')
    tipo = models.CharField(max_length=3,choices=tipfile)
    enlace = models.TextField(validators=[URLValidator()], null=True, blank=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name = ('Bienvenida')
        verbose_name_plural = ('Bienvenidas')
        ordering = ['updated']
    def __str__(self): 
        return self.titulo