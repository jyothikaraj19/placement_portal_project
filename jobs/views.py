from django.shortcuts import render, get_object_or_404
from .models import Job, Application

def home(request):
    jobs = Job.objects.all()
    return render(request, 'home.html', {'jobs': jobs})

def apply_job(request, job_id):
    job = get_object_or_404(Job, id=job_id)
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        resume_link = request.POST.get('resume_link')
        Application.objects.create(job=job, name=name, email=email, resume_link=resume_link)
        return render(request, 'success.html')
    return render(request, 'apply.html', {'job': job})