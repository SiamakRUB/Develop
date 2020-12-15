
from django.shortcuts import render


# Create your views here.

# def home (request) :

#     model=Drivers.objects.all()
#     context={'model':model}
#     return render(request, "ShowData.Html", context)

def Index(request):

    context = {'model': "HomePage"}
    return render(request, "Index.html", context)
