from django.shortcuts import render
from django.http import HttpResponse

def MainSearch (request) :
    
    context={'model':"Main Search"}
    return render(request, "MainSearch.Html", context)