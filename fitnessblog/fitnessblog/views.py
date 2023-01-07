from django.http import HttpResponse


def about(response):
    return HttpResponse('This is the about page')


def home(response):
    return HttpResponse('This is the home page')