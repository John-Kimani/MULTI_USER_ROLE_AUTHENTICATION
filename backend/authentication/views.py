from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics, status
from rest_framework.response import Response

def index(request):
    return HttpResponse('Authentication app works')


class HelloAuthView(generics.GenericAPIView):
    def get(self, request):
        return Response(data={"message": "Hello Auth"}, status=status.HTTP_200_OK)