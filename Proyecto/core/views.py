from django.shortcuts import render,redirect
from .forms import ProductoForm
from django.contrib.auth.decorators import user_passes_test
from django.db.models import Q
from .models import *

def is_admin(user):
    return user.is_authenticated and user.is_staff

def index(request):
    return render (request, 'index.html')



def qs(request):
    return render (request, 'QuienesSomos.html')


def cartas(request):

        cartas = Producto.objects.all()
        cartas2=Categoria.objects.all()
        return render (request, 'cartas.html',{'Cartas':cartas,'Cartas2':cartas2})


def edicion(request):
    return render (request, 'edicionesmitos.html')


def sagrada(request):
    return render (request, 'espada.html')

def dana(request):
    return render (request, 'daana.html')

def imperio(request):
    return render (request, 'helenica.html')

def servicios(request):
    return render (request, 'Servicios.html')


def eventos(request):
    return render (request, 'Eventos.html')

def imperiohelenica(request):
    return render (request, 'ImperioHelenica.html')



#crud
#ver los productos ingresados
@user_passes_test(is_admin, login_url='index')
def ver(request):
    producto=Producto.objects.all()
    categorias = Categoria.objects.all()
    queryset = request.GET.get("buscar")
    categoria = request.GET.get("categoria")
    precio_min = request.GET.get("precio_min")
    precio_max = request.GET.get("precio_max")
    print(queryset)

    if queryset:
        producto = Producto.objects.filter(
            Q(nombre_P__icontains = queryset) |
            Q(descripcion__icontains= queryset)
        ).distinct()

    if categoria:
        producto = producto.filter(id_Categoria=categoria)

    if precio_min and precio_max:
        producto = producto.filter(precio__range=(precio_min,precio_max))

    return render(request,'CRUD/CRUD.html',{'producto':producto,'categorias':categorias})

@user_passes_test(is_admin, login_url='index')
#agregar
def Productform(request):
    if request.method == 'POST':
        formulario = ProductoForm(request.POST, request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect('Crud')
    else:
        formulario = ProductoForm()  # Crea una instancia del formulario
        
    return render(request, 'CRUD/AgregarProducto.html', {'formulario_c': formulario})  # Pasa la instancia del formulario al contexto

#eliminar
@user_passes_test(is_admin, login_url='index')
def eliminar(request, id):
    producto = Producto.objects.get(id_Producto=id)
    producto.delete()
    return redirect('Crud')


@user_passes_test(is_admin, login_url='index')
def Modificar(request, id):
    producto=Producto.objects.get(id_Producto=id)
    datos ={
        'form' :ProductoForm(instance=producto)
    }
    if request.method == "POST":
        formulario2=ProductoForm(data=request.POST,instance=producto,files=request.FILES)
        if formulario2.is_valid():
           formulario2.save()
           return redirect('Crud')
    else:
        formulario2=ProductoForm()
    
    return render(request, 'CRUD/Modificar.html', datos)

