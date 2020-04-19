from django.urls import path
from . import views
from Controller import SampleController
urlpatterns=[
    path('',views.home,name='home') ,
]