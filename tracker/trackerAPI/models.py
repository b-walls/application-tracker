from django.db import models

# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=255)
    website = models.CharField(max_length=255)

class JobPosting(models.Model):
    link = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    company = models.ForeignKey(Company, on_delete=models.PROTECT)

class Application(models.Model):

    STATUS_CHOICES = [
        ("SAVED", "Saved (not applied)"),
        ("APPLIED", "Applied"),
        ("INTERVIEW", "Interviewing"),
        ("OFFER", "Offer"),
        ("REJECTED", "Rejected"),
        ("ACCEPTED", "Accepted"),
    ]

    REMOTE_CHOICES = [
        ("REMOTE", "Remote"),
        ("HYBRID", "Hybrid"),
        ("ONSITE", "On-site"),
    ]

    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="SAVED")
    job_title = models.CharField(max_length=255)
    posting = models.ForeignKey(JobPosting, on_delete=models.CASCADE)
    remote = models.CharField(max_length=20, choices=REMOTE_CHOICES, default="ONSITE")
    date = models.DateField(auto_now=True)

    
