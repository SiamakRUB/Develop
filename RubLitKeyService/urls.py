from django.urls import path
from . import views
from Controller import MainSearchController
from ModelViews import SearchViewModel
urlpatterns=[
    path('',views.Index,name='Index') ,
    path('MainSearch/',MainSearchController.MainSearch,name='MainSearch') ,
]