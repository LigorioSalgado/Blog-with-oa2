from rest_framework import serializers
from .models import User

class UserFirstSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('nombre','apaterno','amaterno','email','is_active')
        #fields = ('__ALL__')

class UserSecondSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        exclude = ('genero',)
