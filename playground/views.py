from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
# Request -> response
# request handler
# action
def say_hello(request):
    return HttpResponse('Hello, World!')


def loremIpsum(request):
    return render(request, 'lorem_ipsum.html')


def about(request):
    return render(request, 'about.html')
