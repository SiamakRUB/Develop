from django.shortcuts import render
from django.http import HttpResponse
from RubLitKeyService import models
from ModelViews import SearchViewModel

def MainSearch (request) :
    inp_target=""
    words=models.Tbltypebase.objects.filter(target="")
    if  request.method == "POST":
        form = SearchViewModel.SearchItem(request.POST)
        if form.is_valid():
            Target = form.cleaned_data['Target']
            inp_target=Target
            # TargetSelects = form.cleaned_data['TargetSelects']
            # OrigSelects = form.cleaned_data['OrigSelects']
            Orig = form.cleaned_data['Orig']
    else:
        form = SearchViewModel.SearchItem()

    if  inp_target:
        words= models.Tbltypebase.objects.filter(target=inp_target)
    context={'wordsModel':words, 'form':form}
    return render(request, "MainSearch.Html", context)

 