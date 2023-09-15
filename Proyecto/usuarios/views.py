
from django.http import HttpResponseRedirect
from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.contrib import messages

from django.views.decorators.csrf import csrf_protect
from django.views.generic.edit import FormView
from django.contrib.auth import login,logout
from .forms import FormularioLogin
from django.contrib.auth import authenticate
from .forms import FormularioUsuario,REGIONES_CHILE



class Login(FormView):
    template_name='Login.html'
    form_class = FormularioLogin
    success_url=reverse_lazy("index")

    @method_decorator(csrf_protect)
    @method_decorator(never_cache)

    def dispatch(self,request,*args,**kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(self.get_success_url())
        else:
            return super(Login,self).dispatch(request,*args,** kwargs)
    def form_valid(self,form):
        login(self.request,form.get_user())                               
        return super(Login,self).form_valid(form)
    

def LogOutUsuario(request):
    logout(request)
    return HttpResponseRedirect('/accounts/login/')
        

from django.contrib.auth import login, authenticate

def crearusuario(request):
    data = {'form': FormularioUsuario()}
    
    if request.method == 'POST':
        formulario = FormularioUsuario(data=request.POST, files=request.FILES)
        
        if formulario.is_valid():
            # Obtiene el valor del campo region del formulario (código numérico)
            codigo_region = formulario.cleaned_data.get("region")
            
            # Mapea el código numérico al nombre de la región usando el diccionario REGIONES_CHILE
            nombre_region = dict(REGIONES_CHILE).get(codigo_region)
            
            # Crea el usuario sin guardarlo en la base de datos todavía
            user = formulario.save(commit=False)
            
            # Asigna el nombre de la región al usuario
            user.region = nombre_region
            
            # Ahora guarda el usuario en la base de datos
            user.save()
            
            username = formulario.cleaned_data.get("username")
            password = formulario.cleaned_data.get("password1")
            account = authenticate(username=username, password=password)
            
            if account is not None:
                login(request, account)
                return redirect("index")
        else:
            print(formulario.errors)
            data["form"] = formulario

    return render(request, 'registro.html', data)








    