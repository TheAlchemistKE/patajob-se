from django.http import HttpResponse


def index(request):
    return HttpResponse('Returns All Job Openings of a Company')


def edit_company_details(request, **args):
    return HttpResponse('Edits A Company\'s details')


def details(request):
    return HttpResponse('Company Details Form')
