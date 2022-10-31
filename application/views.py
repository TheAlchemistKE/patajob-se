from django.shortcuts import render, redirect
from .models import Application
from .forms import ApplicationForm
from job.models import Job

# Create your views here.


def index(request):
    if request.method == 'POST':
        form = ApplicationForm(request.POST)
        if form.is_valid():
            application = Application.objects.create()
            application.save()
            job = Job.objects.get(id=job_id)
            redirect('job_listing')
        return render(request, 'application/apply.html', {'application': application, 'job': job, 'form': form})
    else:
        form = ApplicationForm()
        return render(request, 'application/apply.html', {'form': form})


