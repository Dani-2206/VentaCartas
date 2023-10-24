from django import forms
from django.forms import ModelForm
from .models import *


class ProductoForm(ModelForm):
    

    class Meta:
        
        model=Producto
        fields=['id_Producto','nombre_P','descripcion','imagen','precio','id_Categoria','id_Tipo']
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


