from django.http import HttpResponse


def index(request):
    return HttpResponse('Returns All Job applications of a applicant')


def edit_applicant_details(request, **args):
    return HttpResponse('Edits A applicant\'s details')


def details(request):
    return HttpResponse('applicant Details Form')
