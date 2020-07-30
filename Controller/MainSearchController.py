from django.shortcuts import render
from django.http import HttpResponse
from RubLitKeyService import models
from ModelViews import SearchViewModel
from django.db.models import Max
from django.db.models import Min

def MainSearch (request) :
    inp_target=""
     
    resultmodel=models.Tbltypebase.objects.filter(target="Aufzupassen").union(models.Tbltokenbase.objects.filter(target="Aufzupassen").only("target"))

    if  request.method == "POST":
        form = SearchViewModel.SearchItem(request.POST)
        if form.is_valid():
            Lemma= form.cleaned_data['Lemma']
            OrigSelect= form.cleaned_data['OrigSelect']
            Orig= form.cleaned_data['Orig']
            TargetSelect= form.cleaned_data['TargetSelect']
            Target = form.cleaned_data['Target']
            LemmaSelect= form.cleaned_data['LemmaSelect']
            max_lemma_freq= form.cleaned_data['max_lemma_freq']
            min_lemma_freq= form.cleaned_data['min_lemma_freq']
            max_lemma_absolute= form.cleaned_data['max_lemma_absolute']
            min_lemma_absolute= form.cleaned_data['min_lemma_absolute']
            max_lemma_Zipf= form.cleaned_data['max_lemma_Zipf']
            min_lemma_Zipf= form.cleaned_data['min_lemma_Zipf']
            max_word_phonemes= form.cleaned_data['max_word_phonemes']
            min_word_phonemes= form.cleaned_data['min_word_phonemes']
            max_word_graphemes= form.cleaned_data['max_word_graphemes']
            min_word_graphemes= form.cleaned_data['min_word_graphemes']
            max_word_syllables= form.cleaned_data['max_word_syllables']
            min_word_syllables= form.cleaned_data['min_word_syllables']
            max_word_morphemes= form.cleaned_data['max_word_morphemes']
            min_word_morphemes= form.cleaned_data['min_word_morphemes']
            min_word_morphemes= form.cleaned_data['min_word_morphemes']
            IsFunktion= form.cleaned_data['IsFunktion']
            IsLexion= form.cleaned_data['IsLexion']
            POSSelect= form.cleaned_data['POSSelect']
            POS= form.cleaned_data['POS']
            SyllableTypeSelect= form.cleaned_data['SyllableTypeSelect']
            SyllableType= form.cleaned_data['SyllableType']
            max_word_absolute= form.cleaned_data['max_word_absolute']
            min_word_absolute= form.cleaned_data['min_word_absolute']
            max_word_freq= form.cleaned_data['max_word_freq']
            min_word_freq= form.cleaned_data['min_word_freq']
            max_word_bigram= form.cleaned_data['max_word_bigram']
            min_word_bigram= form.cleaned_data['min_word_bigram']
            max_word_neighbors= form.cleaned_data['max_word_neighbors']
            min_word_neighbors= form.cleaned_data['min_word_neighbors']
            max_word_OLD20= form.cleaned_data['max_word_OLD20']
            min_word_OLD20= form.cleaned_data['min_word_OLD20']
            ErrorLevel= form.cleaned_data['ErrorLevel']
            ErrorLevelSelected= form.cleaned_data['ErrorLevelSelected']
            KOF= form.cleaned_data['KOF']
            ErrorKOFSelected= form.cleaned_data['ErrorKOFSelected']
            ErrorKOF= form.cleaned_data['ErrorKOF']
            resultmodel=models.Tbltypebase.objects.filter(
                target="Aufzupassen"
                ).union(models.Tbltokenbase.objects.filter(
                    target="Aufzupassen"
                    ).only("target"))
            

            
    # else:
    #     form = SearchViewModel.SearchItem()

    # if  inp_target:
    #     words= models.Tbltypebase.objects.filter(target=inp_target)
    # context={'wordsModel':words, 'form':form}
    minmaxmodel=SearchViewModel.MinMaxSearchValue()
    max_no_phonemes=models.Tbltypebase.objects.aggregate(maxph=Max('no_phonemes'))['maxph']
    min_no_phonemes=models.Tbltypebase.objects.aggregate(minph=Min('no_phonemes'))['minph']
    max_norm=models.Tbltypebase.objects.aggregate(norm=Max('chl_lemma_norm'))['norm']
    min_norm=models.Tbltypebase.objects.aggregate(norm=Min('chl_lemma_norm'))['norm']
    max_abs=models.Tbltypebase.objects.aggregate(abs=Max('chl_lemma_abs'))['abs']
    min_abs=models.Tbltypebase.objects.aggregate(abs=Min('chl_lemma_abs'))['abs']
    max_lemmazipf=models.Tbltypebase.objects.aggregate(abs=Max('lemma_zipf'))['abs']
    min_lemmazipf=models.Tbltypebase.objects.aggregate(abs=Min('lemma_zipf'))['abs']

    minmaxmodel.max_norm=max_norm
    minmaxmodel.min_norm=min_norm
    minmaxmodel.max_abs=max_abs
    minmaxmodel.min_abs=min_abs
    minmaxmodel.max_lemmazipf=max_lemmazipf
    minmaxmodel.min_lemmazipf=min_lemmazipf
    minmaxmodel.max_no_phonemes=max_no_phonemes
    minmaxmodel.min_no_phonemes=min_no_phonemes

 
    max_no_graphemes=models.Tbltypebase.objects.aggregate(maxph=Max('no_graphemes'))['maxph']
    min_no_graphemes=models.Tbltypebase.objects.aggregate(minph=Min('no_graphemes'))['minph']
    max_no_syllables=models.Tbltypebase.objects.aggregate(norm=Max('no_syllables'))['norm']
    min_no_syllables=models.Tbltypebase.objects.aggregate(norm=Min('no_syllables'))['norm']
    max_no_morphemes=models.Tbltypebase.objects.aggregate(abs=Max('no_morphemes'))['abs']
    min_no_morphemes=models.Tbltypebase.objects.aggregate(abs=Min('no_morphemes'))['abs']
    max_chl_type_abs=models.Tbltypebase.objects.aggregate(abs=Max('chl_type_abs'))['abs']
    min_chl_type_abs=models.Tbltypebase.objects.aggregate(abs=Min('chl_type_abs'))['abs']
    
    minmaxmodel.max_no_graphemes=max_no_graphemes
    minmaxmodel.min_no_graphemes=min_no_graphemes
    minmaxmodel.max_no_syllables=max_no_syllables
    minmaxmodel.min_no_syllables=min_no_syllables
    minmaxmodel.max_no_morphemes=max_no_morphemes
    minmaxmodel.min_no_morphemes=min_no_morphemes
    minmaxmodel.max_chl_type_abs=max_chl_type_abs
    minmaxmodel.min_chl_type_abs=min_chl_type_abs

    max_chl_type_norm=models.Tbltypebase.objects.aggregate(maxph=Max('chl_type_norm'))['maxph']
    min_chl_type_norm=models.Tbltypebase.objects.aggregate(minph=Min('chl_type_norm'))['minph']
    max_chl_bigram_sum=models.Tbltypebase.objects.aggregate(norm=Max('chl_bigram_sum'))['norm']
    min_chl_bigram_sum=models.Tbltypebase.objects.aggregate(norm=Min('chl_bigram_sum'))['norm']
    max_chl_nei_n=models.Tbltypebase.objects.aggregate(abs=Max('chl_nei_n'))['abs']
    min_chl_nei_n=models.Tbltypebase.objects.aggregate(abs=Min('chl_nei_n'))['abs']
    max_chl_nei_OLD20=models.Tbltokenbase.objects.aggregate(abs=Max('chl_nei_old20'))['abs']
    min_chl_nei_OLD20=models.Tbltokenbase.objects.aggregate(abs=Min('chl_nei_old20'))['abs']

    minmaxmodel.max_chl_type_norm=max_chl_type_norm
    minmaxmodel.min_chl_type_norm=min_chl_type_norm
    minmaxmodel.max_chl_bigram_sum=max_chl_bigram_sum
    minmaxmodel.min_chl_bigram_sum=min_chl_bigram_sum
    minmaxmodel.max_chl_nei_n=max_chl_nei_n
    minmaxmodel.min_chl_nei_n=min_chl_nei_n
    minmaxmodel.max_chl_nei_OLD20=max_chl_nei_OLD20
    minmaxmodel.min_chl_nei_OLD20=min_chl_nei_OLD20
    # no_graphemes
    # no_syllables
    # no_morphemes
    # chl_type.abs
    # chl_type.norm
    # chl_bigram.sum
    # chl_nei.n
    # chl_nei.OLD20
    

    
    

    context={'result':resultmodel,
    'maxminModel':minmaxmodel,
    }
    return render(request, "MainSearch.Html", context)

 