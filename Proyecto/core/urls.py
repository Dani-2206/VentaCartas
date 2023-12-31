from django.urls import path
from django.contrib.auth.decorators import login_required

from .views import *
from usuarios.views import crearusuario

urlpatterns=[

    path('quienesS',qs,name='info'),
    path('dana',dana,name='dana'),
    path('productform',Productform, name='productform'),
    path('crud',login_required(ver),name='Crud'),
    path('elimina/<id>', login_required(eliminar),name="eliminar"),
    path('modificar/<id>', login_required(Modificar),name="modificar"),
    path('registro',crearusuario,name="registro"),
    path('servicios',servicios,name='servicios'),
    path('eventos',eventos,name='eventos'),
    path('infoCarta/<id>', infoCarta, name="infoCarta"),
    path('tipo/<int:tipo_carta>/', tipo, name="tipo"),
    path('pago', pago_realizado, name="pago_realizado"),
    path('infoU',infoU, name="infoU"),
    path('Ventas',VerCompras, name="VerCompras"),
    path('venta/<int:id_Venta>/', ModificarVenta, name="ModificarVenta"),
    path('torneo',torneo,name='torneo'),
    path('VerEventos',VerEventos,name='VerEventos'),
    path('AgregarEvento',AgregarEvento,name="AgregarEvento"),
    path('modificar_evento/<int:id_evento>/', ModificarEvento, name='modificar_evento'),
    path('eliminar_evento/<int:id>/', EliminarEvento, name='eliminar_evento'),
    path('noticiayugi',noticiayugi,name='noticiayugi'),
    path('noticiamitos',noticiasmitos,name='noticiamitos'), 
    path('noticias',noticias,name='noticias'),
    path('torneoyugioh',torneoyugioh,name='torneoyugioh'),
    path('torneomito',torneomito,name='torneomito'),




    
    






  





     

   
]