from rest_framework import serializers
from .models import Company, Application, JobPosting

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = "__all__"

class JobPostingSerializer(serializers.ModelSerializer):
    company = CompanySerializer()

    class Meta:
        model = JobPosting
        fields = ['link', 'location', 'company']

class ApplicationSerializer(serializers.ModelSerializer):
    posting = JobPostingSerializer()
    
    class Meta:
        model = Application
        fields = ['status', 'job_title', 'remote', 'date', 'additional_steps', 'posting']
        depth = 1
