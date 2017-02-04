from django.conf.urls import url
from .views import Index,Contacto,Otros

urlpatterns = [
    url(r'^$', Index, name='index'),
    url(r'^contacto$', Contacto, name='contacto'),
    url(r'^otros/(?P<num>[0-9]+)/(?P<num2>[0-9]+)/$', Otros, name='otros')
    #url(r'^$', admin.site.urls),
]
