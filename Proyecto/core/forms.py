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

            'precio': forms.NumberInput(attrs={'class': 'controls', 'id': 'PrecioEvento', 'name': 'PrecioEvento', 'placeholder': 'Ingrese el precio del Producto'}),

        
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


class ProductEventos(ModelForm):
    
    class Meta:
        model = Evento
        fields = [
            'nombre',
            'descripcion',
            'fecha',
            'hora',
            'precio',
            'foto',
        ]
        labels = {
            'nombre': "Ingrese el nombre del evento",
            'descripcion':"Ingrse una descripcion",
            'fecha': "Ingrese la fecha del evento",
            'hora':'ingrese la hora',
            'precio': "Ingrese el precio del Evento",
            'foto': "Ingrese una foto",
        }

        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'controls', 'id': 'NombrePersona', 'name': 'NombrePersona', 'placeholder': 'Ingrese el nombre del evento'}),
            'descripcion': forms.Textarea(attrs={'class': 'controls', 'id': 'descripcion', 'name': 'descripcion', 'placeholder': 'descripcion'}),
            'fecha': forms.DateTimeInput(attrs={'class': 'controls', 'id': 'FechaEvento', 'name': 'FechaEvento', 'placeholder': 'Ingrese la fecha del evento'}),
            'hora': forms.TimeInput(
            attrs={'class': 'controls', 'placeholder': 'Seleccione la hora'},
            format='%H:%M',  # Formato de hora de 24 horas
            ),
            'precio': forms.NumberInput(attrs={'class': 'controls', 'id': 'PrecioEvento', 'name': 'PrecioEvento', 'placeholder': 'Ingrese el precio del evento'}),
            'foto': forms.ClearableFileInput(attrs={'class': 'controls', 'id': 'FotoEvento', 'name': 'FotoEvento'}),
        }
