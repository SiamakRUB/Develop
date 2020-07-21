
from django import forms


class SearchItem(forms.Form):
    # TargetSelects=('choos','Start with','Endwith','end with')
    Target= forms.CharField(required=False, label="Target",max_length=200)
    # OrigSelects=(required=False,'choos','Start with','Endwith','end with')
    Orig=forms.CharField(required=False,label="Orig",max_length=200)
    # Age: forms.IntegerField(50) 
    # StudentID: 
    # Nationality: str
    # ErrorLevel: str
    # Pos: str
    