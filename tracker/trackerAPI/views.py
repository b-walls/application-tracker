from django.shortcuts import render
from rest_framework import generics
from .serializers import ApplicationSerializer
from .models import Application

class ApplicationView(generics.ListCreateAPIView):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer

