
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
#from django.contrib.auth.views import LoginView,logout_then_login
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required
from core.views import *
from usuarios.views import Login,LogOutUsuario


urlpatterns = [
    path('admin/', admin.site.urls),
    path('paginas/', include('core.urls')),
    path('',index,name='index'),
   # path('accounts/login/',LoginView.as_view(template_name='Login.html'), name='login'),
    path('accounts/login/',Login.as_view(),name="login"),
    path('logout/',login_required(LogOutUsuario), name='logout')



]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

