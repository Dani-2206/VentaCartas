from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from .models import Usuario


REGIONES_CHILE = (
    ('1', 'Arica y Parinacota'),
    ('2', 'Tarapacá'),
    ('3', 'Antofagasta'),
    ('4', 'Atacama'),
    ('5', 'Coquimbo'),
    ('6', 'Valparaíso'),
    ('7', "Bernardo O'Higgins"),  # Cambio del nombre de O'Higgins
    ('RM', 'Metropolitana de Santiago'),
    ('8', 'Maule'),
    ('9', 'Biobío'),
    ('10', 'Araucanía'),
    ('11', 'Los Ríos'),
    ('12', 'Los Lagos'),
    ('13', 'Aysén'),
    ('14', 'Magallanes'),
    ('15', 'Antártica Chilena'),
     
)



class FormularioLogin(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(FormularioLogin,self).__init__(*args,**kwargs)
        self.fields['username'].widget.attrs['class']='form-control','required'
        self.fields['username'].widget.attrs['placeholder']='Nombre De usuario'

        self.fields['password'].widget.attrs['class']='form-control','required'
        self.fields['password'].widget.attrs['placeholder']='Contraseña'

class FormularioUsuario(UserCreationForm):
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Ingrese su contraseña ',
            'id': 'password1',
            'required': 'required',
            'minlength': '5',  # Corrección aquí: de 'min_lenght' a 'minlength'
        }
    ))

    password2 = forms.CharField(label='Contraseña de Confirmación', widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Ingrese nuevamente su contraseña',
            'id': 'password2',
            'required': 'required',
            'minlength': '5',  # Corrección aquí: de 'min_lenght' a 'minlength'
        }
    ))

    region = forms.ChoiceField(label='Región', choices=REGIONES_CHILE, widget=forms.Select(
        attrs={
            'class': 'form-control',
            'id': 'region',
        }
    ))

    class Meta:
        model = Usuario
        fields = ('username', 'nombres', 'apellidos', 'email', 'direccion','telefono', 'foto')
        label = {
            'username':'usename', 
            'nombres':'Nombre',
            'apellidos':'Apellido',
            'email':'Email',
            'direccion':'Direccion',
            'telefono':'Telefono',
            'foto':'Foto'
        }

        widgets = {
            'username': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese Nombre usuario',
                    'id': 'Nombre_u',
                    'required': 'required',
                }
            ),
            'nombres': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese su nombre',
                    'id': 'Nombre',
                    'required': 'required',
                }
            ),
            'apellidos': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese su apellido',
                    'id': 'apellido',
                    'required': 'required',
                }
            ),
            'email': forms.EmailInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese su correo electrónico',
                    'id': 'Correo',
                    'required': 'required',
                }
            ),
            'direccion': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese su Dirección',
                    'id': 'direccion',
                    'required': 'required',
                }
            ),
            'region': forms.ChoiceField(
                label='Región',
                        widget=forms.HiddenInput(),
            ),
            'telefono': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese su teléfono',
                    'id': 'Telefono',
                    'required': 'required',
                }
            ),
            'foto': forms.ClearableFileInput(attrs={'class': 'controls'}),  # Corrección aquí: de 'imagen' a 'foto'
        }