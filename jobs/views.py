from django.shortcuts import render
from .models import Job, Application


def home(request):
    jobs = Job.objects.all()
    return render(request, 'jobs/home.html', {'jobs': jobs})


def job_detail(request, id):
    job = Job.objects.get(id=id)
    return render(request, 'jobs/job_detail.html', {'job': job})


def apply_job(request, id):
    job = Job.objects.get(id=id)

    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        resume = request.FILES['resume']

        Application.objects.create(
            job=job,
            name=name,
            email=email,
            resume=resume
        )

        return render(request, 'jobs/application_success.html', {'job': job})

    return render(request, 'jobs/apply.html', {'job': job})