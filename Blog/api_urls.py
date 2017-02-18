from django.conf.urls import url,include
from django.contrib import admin
from django.conf import settings
#from django.conf.urls.static import static


urlpatterns = [
    url(r'^users/', include('modules.Usuarios.urls_api')),
    url(r'^publicaciones/', include('modules.Publicaciones.urls_api')),
     url(r'^o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    #TODO agregar publicaciones
]
