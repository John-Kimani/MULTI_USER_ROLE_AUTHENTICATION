from django.shortcuts import render
from django.contrib.auth import authenticate
from django.http import HttpResponse
from rest_framework import generics, status, permissions
from rest_framework.response import Response
from rest_framework.request import Request
from .serializers import SignUpSerializer, UserSerializer
from drf_yasg.utils import swagger_auto_schema
from rest_framework.views import APIView

def index(request):
    return HttpResponse('Authentication app works')


class HelloAuthView(generics.GenericAPIView):
    @swagger_auto_schema(operation_summary='Hello Auth application')
    def get(self, request):
        return Response(data={"message": "Hello Auth"}, status=status.HTTP_200_OK)
    

class SignUpUserView(generics.GenericAPIView):
    serializer_class = SignUpSerializer

    @swagger_auto_schema(operation_summary='Create a user account')
    def post(self, request:Request):
        data = request.data 

        serializer = self.serializer_class(data=data)

        if serializer.is_valid():
            serializer.save()

            response = {
                "message": "New user created successfully",
                "data":serializer.data
            }
            return Response(data=response, status=status.HTTP_201_CREATED)
        
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class RetrieveUserView(APIView):
  permission_classes = [permissions.IsAuthenticated]

  def get(self, request):
    user = request.user
    user = UserSerializer(user)

    return Response(user.data, status=status.HTTP_200_OK)

class LoginView(APIView):
    def post(self, request:Request):
        email = request.data.get('email')
        password = request.data.get('password')

        user = authenticate(email=email, password=password)

        if user is not None:

            response = {
                "message": "Login success",
                "token": user.auth_token.key
            }
            return Response(data=response, status=status.HTTP_200_OK)
        else:
            return Response(data={"message": "Invalid email or password"})


    def get(self, request:Request):
        content = {
            "user": str(request.user),
            "auth": str(request.auth)
        }

        return Response(data=content, status=status.HTTP_200_OK)