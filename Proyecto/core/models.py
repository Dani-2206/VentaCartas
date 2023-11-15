from django.db import models
class Tipo(models.Model):
    id_Tipo=models.AutoField(primary_key=True,verbose_name="ID de categoria")
    nombre_Tipo=models.CharField(verbose_name="ID del producto",max_length=20)

    def __str__(self):
        return(self.nombre_Tipo)


class Categoria(models.Model):
    id_Categoria=models.AutoField(primary_key=True,verbose_name="ID de categoria")
    nombre_Categoria=models.CharField(verbose_name="ID del producto",max_length=20)
    def __str__(self):
        return(self.nombre_Categoria)
    
    
class Producto(models.Model):
    id_Producto = models.AutoField(primary_key=True, verbose_name="ID del producto")
    nombre_P = models.CharField(verbose_name="Nombre del producto", max_length=20)
    descripcion = models.TextField(verbose_name="Descripción")
    imagen = models.ImageField(verbose_name="Foto de la carta", upload_to='productos/')
    precio = models.IntegerField(verbose_name='Precio del Producto')
    id_Categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    id_Tipo = models.ForeignKey(Tipo, on_delete=models.CASCADE, default=1)

   
   

    def __str__(self):
        return self.nombre_P
    


class Venta(models.Model):
    id_Venta = models.AutoField(primary_key=True, verbose_name="ID del producto")
    nombre=models.CharField(verbose_name="Nombre DEl comprador", max_length=20)
    nombre_usuario=models.CharField(verbose_name="Nombre DEl comprador", max_length=20,default="")
    fecha= models.CharField(verbose_name="fecha ", max_length=50)
    email= models.CharField(verbose_name="Email", max_length=50)
    productos=models.TextField(verbose_name="Productos Seleccionados",default="")
    total= models.IntegerField(verbose_name='total del producto',default=0)
    direccion =models.CharField(verbose_name="Email", max_length=50, default="")
    region =models.CharField(verbose_name="Email", max_length=50, default="")
    estado=models.CharField(verbose_name='Estado del producto ',max_length=20,default="en tienda")
    def __str__(self):
        return self.nombre


