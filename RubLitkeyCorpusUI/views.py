from django.shortcuts import render
from django.http import HttpResponse
# from ModelViews.MenuModelView import MenuItem
from .models import sample
# Create your views here.
#  views are equal Controller in MVC


def home(request):
    # model= MenuItem()
    # model.Name="SampleName"
    # model.text="SampleText"
    # model.link="http://google.com"
    return render(request, "MainPage.html", {'name': '  Siamak  ', 'model': 'model'})


def menu(request):
    return render(request, "Menu.html", {'name': '  Click to View   '})

# def Sample_getItems (request) :
    # model= drivers.objects.all()

    # model.FirstName="SampleText"
    # model.LastName="SampleText"
    # model.UserName="http://google.com"
    # model.RecordCreated="http://google.com"
    # model.Address="http://google.com"

    # return render(request, "ShowData.Html",{'model':model})
