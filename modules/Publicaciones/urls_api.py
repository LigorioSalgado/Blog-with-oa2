from django.conf.urls import url
from .api_views import PublicacionList,PublicacionDetail

urlpatterns = [
    url(r'^$', PublicacionList.as_view()),
    url(r'^(?P<pk>[0-9]+)/$', PublicacionDetail.as_view()),

]
