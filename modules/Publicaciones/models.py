from django.db import models
from django.contrib.auth.models import User


TAGS = (
        ('TC','Tecnología'),
        ('CT','Científico'),
        ('PR','Programación')
)

class PepePublicacionesManager(models.Manager):

    def get_queryset(self):
        return super(PepePublicacionesManager,self).get_queryset().filter(autor__username="Pepe")

class Publicacion (models.Model):
    id  = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=80)
    contenido = models.TextField()
    fecha  = models.DateField(auto_now_add=True)
    autor = models.ForeignKey(User,on_delete=models.CASCADE)
    tags = models.CharField(choices=TAGS,max_length=50)


    pepe_publish = PepePublicacionesManager()

    def __str__(self):
        return "%s %s" % ("Publicacion: ",self.nombre)
