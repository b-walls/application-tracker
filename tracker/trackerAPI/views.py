from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from .serializers import ApplicationSerializer
from .models import Application

def home_view(request):
    return render(request, "home.html")

class ApplicationView(generics.ListCreateAPIView):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer

