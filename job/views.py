from django.conf import settings
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

import os

from applicant.resume_parser import summarize_resume
from job.match import calculate_match_score, analyze_job_description
from job.models import Job
from application.models import Application


class JobListView(ListView):
    model = Job
    template_name = 'job/jobs.html'
    context_object_name = 'jobs'
    ordering = ['-created_at']


class JobDetailView(DetailView):
    model = Job
    template_name = 'job/job_details.html'


summary = summarize_resume(
    '/Users/kelyn_njeri/Desktop/Projects/Personal/DjangoProjects/patajob/job/Kelyn Njeri - Software Engineer.pdf')
job_summary = summarize_resume(
    '/Users/kelyn_njeri/Desktop/Projects/Personal/DjangoProjects/patajob/job/Job Description.pdf')


def apply_to_job(request, job_id):
    job = Job.objects.get(id=job_id)
    score = match(job_id)
    application = Application(job_id=job, applicant_id=request.user, applicant_match_score=score)
    application.save()
    return render(request, 'application/index.html', {'application': application, 'job': job})


def match_insight(request, job_id):
    job = Job.objects.get(id=job_id)
    resume_summary = summary
    job_description_summary = analyze_job_description(job.role_entails)[1]

    score = calculate_match_score(
        job_description_summary['technical_skills'],
        resume_summary['candidate_keywords']['technical_skills'])
    tech_skills = resume_summary['candidate_keywords']['technical_skills']
    soft_skills = resume_summary['candidate_keywords']['soft_skills']

    return render(request, 'applicant/index.html', {'score': score, 'technical_skills': tech_skills, 'soft_skills': soft_skills})


def match(job_id):
    job = Job.objects.get(id=job_id)
    resume_summary = summary
    job_description_summary = analyze_job_description(job.role_entails)[1]

    score = calculate_match_score(
        job_description_summary['technical_skills'],
        resume_summary['candidate_keywords']['technical_skills'])

    return score

