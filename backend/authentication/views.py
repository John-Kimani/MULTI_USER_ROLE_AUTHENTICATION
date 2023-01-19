from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.request import Request
from .serializers import SignUpSerializer
from drf_yasg.utils import swagger_auto_schema

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