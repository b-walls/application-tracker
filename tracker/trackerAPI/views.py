from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from .serializers import ApplicationSerializer, CompanySerializer, JobPostingSerializer
from .models import Application, Company, JobPosting

def home_view(request):
    return render(request, "home.html")

class ApplicationView(generics.ListCreateAPIView):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer

class SingleApplicationView(generics.RetrieveAPIView):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer

class CompanyCreateView(generics.CreateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

class PostingCreateView(generics.CreateAPIView):
    queryset = JobPosting.objects.all()
    serializer_class = JobPostingSerializer


