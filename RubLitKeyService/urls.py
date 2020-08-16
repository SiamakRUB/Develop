from django.urls import path
from django.conf.urls import url
from . import views
from Controller import MainSearchController
from ModelViews import SearchViewModel
urlpatterns=[
    path('',views.Index,name='Index'),
    path('MainSearch/',MainSearchController.MainSearch,name='MainSearch'),
    path('ShowGroupSetting/',MainSearchController.ShowGroupSetting,name='ShowGroupSetting'),
    url(r'^ajax/ShowGroupSetting/$', MainSearchController.ShowGroupSetting, name='validate_username')
]