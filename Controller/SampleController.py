from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def add(request):  # code convention Sample_add
    val1 = int(request.GET["num1"])
    val2 = int(request.GET["num2"])
    res = val1+val2

    return render(request, "Result.Html", {'res': res})


def Save(request):
    val1 = int(request.POST["num1"])
    val2 = int(request.POST["num2"])
    res = val1+val2

    return render(request, "Result.html", {'res': res, 'done': 'is Done'})
