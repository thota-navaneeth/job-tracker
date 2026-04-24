from django.shortcuts import render, redirect
from .models import JobApplication, User
from .forms import JobApplicationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import get_object_or_404
# Create your views here.
def home(request):
    if request.user.is_authenticated:
        return redirect('job_list')
    return render(request, 'tracker/home.html')

@login_required
def job_list(request):
    status = request.GET.get('status')
    if status:
        jobs = JobApplication.objects.filter(user=request.user, status=status)
    else:
        jobs = JobApplication.objects.filter(user=request.user)
    return render(request, 'tracker/job_list.html', {'jobs': jobs})

@login_required
def add_job(request):
    if request.method == 'POST':
        form = JobApplicationForm(request.POST)
        if form.is_valid():
            job = form.save(commit=False)
            job.user = request.user
            job.save()
            return redirect('job_list')
    else:
        form = JobApplicationForm()
        
    return render(request, 'tracker/add_job.html', {'form': form})

def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login/')
    else:
        form = UserCreationForm()
    
    return render(request, 'tracker/signup.html', {'form': form})


@login_required
def edit_job(request, id):
    job = get_object_or_404(JobApplication, id=id, user=request.user)

    if request.method =='POST':
        form = JobApplicationForm(request.POST, instance=job)
        if form.is_valid():
            form.save()
            return redirect('job_list')
    else:
        form = JobApplicationForm(instance=job)
    
    return render(request, 'tracker/edit_job.html', {'form': form})

@login_required
def delete_job(request, id):
    job = get_object_or_404(JobApplication, id=id, user=request.user)
    job.delete()
    return redirect('job_list')






