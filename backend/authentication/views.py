from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.request import Request
from .serializers import SignUpSerializer

def index(request):
    return HttpResponse('Authentication app works')


class HelloAuthView(generics.GenericAPIView):
    def get(self, request):
        return Response(data={"message": "Hello Auth"}, status=status.HTTP_200_OK)
    

class SignUpUserView(generics.GenericAPIView):
    serializer_class = SignUpSerializer

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