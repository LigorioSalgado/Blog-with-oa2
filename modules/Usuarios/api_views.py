from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .models import User
from .serializers import *


#Vistas basadas en clases

class UserList(APIView):

    def get(self,request):

        user = User.objects.all()
        serializer = UserSecondSerializer(user,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)


    def post(self,request):

        serializer = UserFirstSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
