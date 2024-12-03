#encoding:utf-8
from django.db import models


#datos de las usuario
class Usuario(models.Model):
    idUsuario = models.AutoField(primary_key=True)
    def __str__(self):
        return 
    
#datos de los pelicula
class Pelicula(models.Model):
    idPelicula = models.AutoField(primary_key=True)
    
    
    def __str__(self):
        return
    
#datos de las categoria
class Categoria(models.Model):
    idCategoria = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)    

    
    def __str__(self):
        return
            
#datos de los ocupacion 
class Ocupacion(models.Model):
    nombre = models.CharField(max_length=100)    
    def __str__(self):
        return self.nombre
        
#datos de los puntuacion 
class Puntuacion(models.Model):
    idUsuario = models.ForeignKey(Usuario, on_delete= models.CASCADE)
    idPelicula = models.ForeignKey(Pelicula, on_delete= models.CASCADE)
    puntuacion = models.SmallIntegerField()
    def __str__(self):
        return self.puntuacion
    
