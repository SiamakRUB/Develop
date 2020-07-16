from django.urls import path
from . import views
from Controller import MainSearchController
urlpatterns=[
    path('',views.Index,name='Index') ,
    path('MainSearch/',MainSearchController.MainSearch,name='MainSearch') ,
]