from  rest_framework import serializers
from .models import Publicacion
from modules.Usuarios.models import User
#from modules.Usuarios.serializers import PublicacionSecondSerializer
class UserSecondSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        exclude = ('genero',)


class PublicacionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Publicacion
        fields = ("nombre","contenido","fecha","tags","autor")

class PublicacionSecondSerializer(serializers.ModelSerializer,serializers.Serializer):
    writer_name = serializers.CharField(source='autor.nombre')
    writer_lastname = serializers.CharField(source='autor.apaterno')
    class Meta:
        model = Publicacion
        fields = ("nombre","contenido","fecha","tags","writer_name","writer_lastname","autor")
