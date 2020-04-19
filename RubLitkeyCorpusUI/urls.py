from django.urls import path
from . import views
from Controller import SampleController
urlpatterns=[

    path('',views.home,name='home') ,
    path('add',SampleController.add,name='add'),
    path('Save',SampleController.Save,name='add'), 
    path('Sample_getItems',views.Sample_getItems,name='getItems') 
    
]