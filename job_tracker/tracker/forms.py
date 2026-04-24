from django import forms
from .models import JobApplication

class JobApplicationForm(forms.ModelForm):
    class Meta:
        model = JobApplication
        fields = ['title', 'company_name', 'status', 'deadline', 'notes']
        widgets = {
            'deadline': forms.DateInput(attrs={'type': 'date'}),
        }