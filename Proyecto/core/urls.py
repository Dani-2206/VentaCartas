from django.urls import path
from django.contrib.auth.decorators import login_required

from .views import *
from usuarios.views import crearusuario

urlpatterns=[
    

    path('quienesS',qs,name='info'),

    path('cartas',cartas,name='cartas'),

    path('edicion',edicion,name='edicion'),

    path('dana',dana,name='dana'),

    path('sagrada',sagrada,name='sagrada'),

    path('imperio',imperio,name='imperio'),

    path('productform',Productform, name='productform'),
    
    path('crud',login_required(ver),name='Crud'),

    path('elimina/<id>', login_required(eliminar),name="eliminar"),
    path('modificar/<id>', login_required(Modificar),name="modificar"),
    path('registro',crearusuario,name="registro"),

    path('servicios',servicios,name='servicios'),

    path('eventos',eventos,name='eventos'),

    path('imperiohelenica',imperiohelenica,name='imperiohelenica')

  





     

   
]