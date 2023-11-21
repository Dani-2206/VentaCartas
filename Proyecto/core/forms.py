from django import forms
from django.forms import ModelForm
from .models import *




class ProductoForm(ModelForm):
    

    class Meta:
        
        model=Producto
        fields=['id_Producto',
                'nombre_P',
                'descripcion',
                'imagen',
                'precio',
                'id_Categoria',
                'id_Tipo']
        labels={
            'id_Producto':'id del producto',
            'nombre_P':'Nombre del producto',
            'descripcion':'Ingrese una descripcion ',
            'imagen':'Imagen',
            'precio':'Ingrese el precio',
            'id_Categoria':'Ingresar la categoria',
            'id_Tipo':'Ingresar el tipo'
        }

        widgets={
            'id_Producto': forms.TextInput(
                attrs={
                    'class': 'controls',
                    'id': 'idProducto',
                    'name': 'idPrdocuto',
                    'placeholder': 'Ingrese el id del producto'
                }
            ),



            'nombre_P': forms.TextInput(
                attrs={
                    'class': 'controls',
                    'id': 'NombreProducto',
                    'name': 'NombreProducto',
                    'placeholder': 'Ingrese el nombre del producto'
                }
            ),


            'descripcion':forms.Textarea(
                    attrs={
                        'class': 'controls',
                        'id': 'descripcion',
                        'name': 'descripcion',
                        'placeholder': 'descripcion'
                    }
            ),
            

            'imagen': forms.ClearableFileInput(attrs={'class': 'controls'}),

            'precio':forms.TextInput(
                attrs={
                    'class': 'controls',
                    'id': 'precio',
                    'name': 'precio',
                    'placeholder': '1000',
                    'required': True
                }
            ),

        
        }



class ProductVentas(ModelForm):
    ESTADOS_CHOICES = (
        ('En tienda', 'En tienda'),
        ('Enviado', 'Enviado'),
        ('Entregado', 'Entregado'),
    )

    estado = forms.ChoiceField(choices=ESTADOS_CHOICES, widget=forms.Select(attrs={'class': 'controls'}))


    class Meta:
        model = Venta
        fields = [
            'nombre',
            'nombre_usuario',
            'fecha',
            'email',
            'productos',
            'total',
            'direccion',
            'region',
            'estado'
        ]

        # Resto del código Meta...

        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'controls', 'id': 'NombrePersona', 'name': 'NombrePersona', 'placeholder': 'Ingrese el nombre de la persona'}),
            'nombre_usuario': forms.TextInput(attrs={'class': 'controls', 'id': 'nombreUsuario', 'name': 'nombreUsuario', 'placeholder': 'Ingrese el nombre del Usuario'}),
            'email': forms.TextInput(attrs={'class': 'controls', 'id': 'Email', 'name': 'Email', 'placeholder': 'Ingrese el email'}),
            'productos': forms.Textarea(attrs={'class': 'controls', 'id': 'Productos', 'name': 'Productos', 'placeholder': 'Productos'}),
            'total': forms.TextInput(attrs={'class': 'controls', 'id': 'Total', 'name': 'Total', 'placeholder': '1000', 'required': True}),
            'direccion': forms.TextInput(attrs={'class': 'controls', 'id': 'direccion', 'name': 'direccion', 'placeholder': 'Ingrese la direccion'}),
            'region': forms.TextInput(attrs={'class': 'controls', 'id': 'region', 'name': 'region', 'placeholder': 'Ingrese la region'}),
            'estado': forms.Select(attrs={'class': 'controls'}),
        }