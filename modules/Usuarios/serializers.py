from rest_framework import serializers
from .models import User
from modules.Publicaciones.serializers import PublicacionSerializer

class UserFirstSerializer(serializers.ModelSerializer):
    publicaciones = PublicacionSerializer(read_only=True,many=True)
    class Meta:
        model = User
        fields = ('nombre','apaterno','amaterno','email','is_active','publicaciones')
        #fields = ('__ALL__')

class UserSecondSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        exclude = ('genero',)
