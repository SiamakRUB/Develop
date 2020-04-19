from django.shortcuts import render
from RubLitKeyService.models import Drivers

# Create your views here.

def home (request) :
    
    model=Drivers.objects.all() 
    context={'model':model}
    return render(request, "ShowData.Html", context)