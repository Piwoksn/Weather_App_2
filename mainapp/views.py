from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return HttpResponse(content="This is my django server")