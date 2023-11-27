from django.shortcuts import render,redirect,get_object_or_404
from .forms import ProductoForm,ProductVentas
from django.contrib.auth.decorators import user_passes_test
from django.http import JsonResponse
import json
from django.db.models import Q



from carro.context_processor import importe_total_carro
from carro.carro import Carro
from .models import *

def is_admin(user):
    return user.is_authenticated and user.is_staff


def index(request):
    Mito = Producto.objects.filter(id_Tipo=1)
    Yugi = Producto.objects.filter(id_Tipo=2)

    return render (request, 'index.html',{'Mito':Mito,'yugi':Yugi})



def qs(request):
    return render (request, 'core/QuienesSomos.html')




def dana(request):

    producto = Producto.objects.all()
    categorias = Categoria.objects.all()
    tipo=Tipo.objects.all()
    queryset = request.GET.get("buscar")
    categoria = request.GET.get("categoria")
    tipo_carta = request.GET.get("TipoCarta")
    precio_min = request.GET.get("precio_min")
    precio_max = request.GET.get("precio_max")

    if queryset:
        producto = producto.filter(
            Q(nombre_P__icontains=queryset) |
            Q(descripcion__icontains=queryset)
        ).distinct()

    if tipo_carta:
        producto = producto.filter(id_Tipo=tipo_carta)



    if categoria:
        producto = producto.filter(id_Categoria=categoria)

    if precio_min and precio_max:
        producto = producto.filter(precio__range=(precio_min, precio_max))

    return render(request, 'core/daana.html', {'producto': producto, 'categorias': categorias,'tipo':tipo})



def servicios(request):
    return render (request, 'core/Servicios.html')


def eventos(request):
    return render (request, 'core/Eventos.html')





def infoCarta(request, id):
    producto = get_object_or_404(Producto, id_Producto=id)
    return render(request, 'core/infoCarta.html', {'carta': producto})


def tipo(request, tipo_carta):
    productos = Producto.objects.filter(id_Tipo=tipo_carta)
    return render(request, 'core/productoEspecifico.html', {'cartas': productos})





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

    return render(request,'CRUD/Productos/CRUD.html',{'producto':producto,'categorias':categorias})

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
        
    return render(request, 'CRUD/Productos/AgregarProducto.html', {'formulario_c': formulario})  # Pasa la instancia del formulario al contexto

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
    
    return render(request, 'CRUD/Productos/Modificar.html', datos)


def pago_realizado(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body.decode('utf-8'))

            nombre_comprador = data.get('comprador', '') # nombre del paypal
            fecha_compra = data.get('fecha', '')  #fecha de la compra
            status_compra = data.get('status', '') #status de la compra
            productos=importe_total_carro(request)
            lista_productos=productos["lista_producto"] # productos que eligio
            total=productos["importe_total_carro"] # total (dinero)

            nombre_usuario = request.user.username # nombre de usuario
            email=request.user.email # email pero de la pagina
            direccion = request.user.direccion
            region = request.user.region




            print(f"Nombre del comprador: {nombre_comprador}")
            print(f"Usuario: {nombre_usuario}")
            print(f"La fecha de la compra: {fecha_compra}")
            print(f"Email: {email}")
            print(f"Status: {status_compra}")
            print(f"Lista Productos: {lista_productos}")
            print(f"Lista Productos: {total}")


            if status_compra == "COMPLETED":
                print("El status de la compra está bien")
                venta = Venta(nombre=nombre_comprador,nombre_usuario=nombre_usuario ,
                              fecha=fecha_compra, email=email,productos=lista_productos,total=total,direccion=direccion,region=region)
                venta.save()
                carro = Carro(request)
                carro.limpiar_carro()

                return JsonResponse({'status': 'success', 'message': 'Orden procesada con éxito'})
            else:
                print("El status de la compra no es COMPLETED")

            return JsonResponse({'status': 'success', 'message': 'Orden procesada con éxito'})

        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)})

    return render(request, 'core/pago.html')

def infoU(request):
    usuario=request.user.username
    info = Venta.objects.filter(nombre_usuario=usuario)
    if info:
        return render(request, 'usuario/infoUsuario.html', {"informacion": info})
    else:
        return render(request, 'usuario/infoUsuario.html', {"informacion": None})


@user_passes_test(is_admin, login_url='index')
def VerCompras(request):
    Ventas=Venta.objects.all()
    return render(request, 'CRUD/Ventas/VerEnvios.html',{"Ventas":Ventas})

@user_passes_test(is_admin, login_url='index')
def ModificarVenta(request, id_Venta):
    productov = Venta.objects.get(id_Venta=id_Venta)

    if request.method == "POST":
        formulario2 = ProductVentas(data=request.POST, instance=productov)
        if formulario2.is_valid():
            formulario2.save()
            return redirect('VerCompras')
    else:
        formulario2 = ProductVentas(instance=productov)

    datos = {'form': formulario2}
    return render(request, 'CRUD/Ventas/ModificarVentas.html', datos)

def evento(request):
    return render (request, 'core/evento.html')

def torneo(request):
    return render (request, 'core/torneomitos.html')


