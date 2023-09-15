from django.db import models


class Categoria(models.Model):
    id_Categoria=models.IntegerField(primary_key=True,verbose_name="ID de categoria")
    nombre_Categoria=models.CharField(verbose_name="ID del producto",max_length=20)
    def __str__(self):
        return(self.nombre_Categoria)
    

class Producto(models.Model):
    id_Producto=models.CharField(primary_key=True,verbose_name="ID del producto",max_length=20)
    nombre_P=models.CharField(verbose_name="ID del producto",max_length=20)
    descripcion=models.TextField(verbose_name="Descripcion")
    imagen = models.ImageField(verbose_name="foto de la carta", upload_to='productos/')
    precio=models.IntegerField(verbose_name='Precio del Producto')
    id_Categoria=models.ForeignKey(Categoria,on_delete=models.CASCADE)

    def __str__(self):
        return(self.nombre)



