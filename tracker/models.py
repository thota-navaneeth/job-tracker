from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class JobApplication(models.Model):
    STATUS_CHOICES = [
        ('APPLIED', 'Applied'),
        ('INTERVIEW', 'Interview'),
        ('REJECTED', 'Rejected'),
        ('OFFER', 'Offer'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    title = models.CharField(max_length=200)
    company_name = models.CharField(max_length=100)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="APPLIED")

    applied_date = models.DateField(auto_now_add=True)
    deadline = models.DateField(null=True, blank=True)

    notes = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} at {self.company_name}"



