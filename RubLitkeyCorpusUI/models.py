from django.db import models
# Create your models here.

class drivers(models.Model):
    Id: models.AutoField()
    FirstName: models.CharField(max_length=200)
    LastName: models.CharField(max_length=200)
    UserName: models.CharField(max_length=200)
    Address: models.CharField(max_length=1000)
    RecordCreated: models.DateField(auto_now=False,auto_now_add=False)
    class Meta:
        db_table="drivers"

class sample:
    id:int        