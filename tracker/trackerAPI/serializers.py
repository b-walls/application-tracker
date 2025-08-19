from rest_framework import serializers
from .models import Company, Application, JobPosting

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = "__all__"

class JobPostingSerializer(serializers.ModelSerializer):
    company = serializers.PrimaryKeyRelatedField(
        queryset=Company.objects.all(),
        write_only=True
    )

    company_details = CompanySerializer(source="company", read_only=True)

    class Meta:
        model = JobPosting
        fields = ['link', 'location', 'company', 'company_details']

class ApplicationSerializer(serializers.ModelSerializer):
    posting = serializers.PrimaryKeyRelatedField(
        queryset=JobPosting.objects.all(),
        write_only=True
    )

    posting_details = JobPostingSerializer(source="posting", read_only=True)

    class Meta:
        model = Application
        fields = [
            'id',
            'status',
            'job_title',
            'remote',
            'date',
            'additional_steps',
            'posting',          
            'posting_details'
        ]
