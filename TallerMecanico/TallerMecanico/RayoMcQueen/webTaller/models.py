from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(primary_key=True,max_length=45)
    foto = models.ImageField(upload_to='foto',null=True)
    
    def __str__(self) -> str:
        return self.nombre
    
class Reparacion(models.Model):
    idReparacion= models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=45)
    #precio = models.IntegerField(default=10)
    descripcion = models.TextField()
    categoria = models.ForeignKey(Categoria,on_delete=models.CASCADE)
    foto=models.ImageField(upload_to='foto',null=True,default='foto/default2.jpg')
    publicar=models.BooleanField(default=False)
    comentario=models.TextField(default='S/C')
    usuario= models.ForeignKey(User,on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.nombre
    
    #en caso de añadirle precio:
    #def __str__(self) -> str:
    #    return self.nombre+" "+str(self.precio)

class Repuesto(models.Model):
    idRepuesto= models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=45)
    precio = models.IntegerField(default=10)
    descripcion = models.TextField()
    categoria = models.ForeignKey(Categoria,on_delete=models.CASCADE)
    foto=models.ImageField(upload_to='foto',null=True,default='foto/default_repuesto.jpg')
    publicar=models.BooleanField(default=False)
    comentario=models.TextField(default='S/C')
    usuario= models.ForeignKey(User,on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.nombre
    
    #en caso de añadirle precio:
    #def __str__(self) -> str:
    #    return self.nombre+" "+str(self.precio)


class Galeria(models.Model):
    idGaleria= models.AutoField(primary_key=True)
    foto = models.ImageField(upload_to='foto')
    reparacion = models.ForeignKey(Reparacion,on_delete=models.CASCADE)

    def __str__(self) -> str:
        return "N°"+str(self.idGaleria)+" / "+self.reparacion.nombre


class Contacto(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    telefono = models.CharField(max_length=20)
    mensaje = models.TextField()

    def __str__(self):
        return self.nombre


#class Carrito(models.Model):
#    nombre = models.CharField(max_length=200)
#    precio = models.IntegerField()
#   cantidad = models.IntegerField(default=0)
#    total = models.IntegerField()

#   def __str__(self):
#       return self.nombre

   