from django.shortcuts import render
from django.http import HttpResponse
from RubLitKeyService import models
from ModelViews import SearchViewModel
from django.db.models import Max
from django.db.models import Min
from django.db.models import Q
from functools import reduce
from RubLitKeyService.models import Tbltokenbase
import operator

def switchStringSelect(selectedvalue):
    switcher = {
        1: "startswith",
        2: "contains",
        3: "endswith",
    }
    func= switcher.get(selectedvalue, "Invalid")
    return func()

def MainSearch (request) :
    inp_target="" 

    resultmodel=models.Tbltokenbase.objects.filter(id__lte=0)
    q_list_type =[]
    q_list_token=[]
    if  request.method == "POST":
        form = SearchViewModel.SearchItem(request.POST)
        if form.is_valid():
            LemmaSelect= int(form.cleaned_data['LemmaSelect'])
            Lemma= form.cleaned_data['Lemma']
            
            if Lemma:
                if LemmaSelect>-1:
                    switcher = {
                    0: Q(chl_lemma=Lemma),
                    1: Q(chl_lemma__startswith=Lemma),
                    2: Q(chl_lemma__contains=Lemma),
                    3: Q(chl_lemma__endswith=Lemma),
                    }
                    q_list_token.append( switcher.get(LemmaSelect, "Invalid"))
                 

            OrigSelect= int(form.cleaned_data['OrigSelect'])
            Orig= form.cleaned_data['Orig']

            if Orig:
                if OrigSelect>-1:
                    switcher = {
                    0: Q(orig=Orig),
                    1: Q(orig__startswith=Orig),
                    2: Q(orig__contains=Orig),
                    3: Q(orig__endswith=Orig),
                    }
                    q_list_token.append( switcher.get(OrigSelect, "Invalid"))

  
            TargetSelect=int( form.cleaned_data['TargetSelect'])
            Target = form.cleaned_data['Target']
            if Target:
                if TargetSelect>-1:
                    switcher = {
                    0: Q(target=Target),
                    1: Q(target__startswith=Target),
                    2: Q(target__contains=Target),
                    3: Q(target__endswith=Target),
                    }
                    q_list_token.append( switcher.get(TargetSelect, "Invalid"))

            IsFunktion= form.cleaned_data['IsFunktion']
            IsLexion= form.cleaned_data['IsLexion']

            POSSelect= int(form.cleaned_data['POSSelect'])
            POS= form.cleaned_data['POS']
            if POS:
                if POSSelect>-1:
                    switcher = {
                    0: Q(pos=POS),
                    1: Q(pos__startswith=POS),
                    2: Q(pos__contains=POS),
                    3: Q(pos__endswith=POS),
                    }
                    q_list_token.append( switcher.get(POSSelect, "Invalid"))

            max_lemma_freq= form.cleaned_data['max_lemma_freq']
            if max_lemma_freq>0:
                q_list_token.append( Q(chl_lemma_norm__lte=max_lemma_freq))
            min_lemma_freq= form.cleaned_data['min_lemma_freq']
            if min_lemma_freq>0:
                q_list_token.append( Q(chl_lemma_norm__gte=min_lemma_freq))
            

            max_lemma_absolute= form.cleaned_data['max_lemma_absolute']
            if max_lemma_absolute>0:
                q_list_token.append( Q(chl_lemma_abs__lte=max_lemma_absolute))

            min_lemma_absolute= form.cleaned_data['min_lemma_absolute']
            if min_lemma_absolute>0:
                q_list_token.append( Q(chl_lemma_abs__gte=min_lemma_freq))

            max_lemma_Zipf= form.cleaned_data['max_lemma_Zipf']
            if max_lemma_Zipf>0:
                q_list_token.append( Q(lemma_zipf__lte=max_lemma_Zipf))

            min_lemma_Zipf= form.cleaned_data['min_lemma_Zipf']
            if min_lemma_Zipf>0:
                q_list_token.append( Q(lemma_zipf__gte=min_lemma_Zipf))

            max_word_phonemes= form.cleaned_data['max_word_phonemes']
            if max_word_phonemes>0:
                q_list_token.append( Q(no_phonemes__lte=max_word_phonemes))
            
        #    ///
            min_word_phonemes= form.cleaned_data['min_word_phonemes']
            if min_word_phonemes>0:
                q_list_token.append( Q(no_phonemes__gte=min_word_phonemes))
            
            max_word_graphemes= form.cleaned_data['max_word_graphemes']
            if max_word_graphemes>0:
                q_list_token.append( Q(no_graphemes__lte=max_word_graphemes))
            min_word_graphemes= form.cleaned_data['min_word_graphemes']
            if min_word_graphemes>0:
                q_list_token.append( Q(no_graphemes__gte=min_word_graphemes))

            max_word_syllables= form.cleaned_data['max_word_syllables']
            if max_word_syllables>0:
                q_list_token.append( Q(no_syllables__lte=max_word_syllables))
            min_word_syllables= form.cleaned_data['min_word_syllables']
            if min_word_syllables>0:
                q_list_token.append( Q(no_syllables__gte=min_word_syllables))

            max_word_morphemes= form.cleaned_data['max_word_morphemes']
            if max_word_morphemes>0:
                q_list_token.append( Q(no_morphemes__lte=max_word_morphemes))
            min_word_morphemes= form.cleaned_data['min_word_morphemes']
            if min_word_morphemes>0:
                q_list_token.append( Q(no_morphemes__gte=min_word_morphemes))
           
            SyllableTypeSelect= form.cleaned_data['SyllableTypeSelect']
            SyllableType= form.cleaned_data['SyllableType']
            if SyllableType:
                if SyllableTypeSelect>-1:
                    switcher = {
                    0: Q(syllable_types=SyllableType),
                    1: Q(syllable_types__startswith=SyllableType),
                    2: Q(syllable_types__contains=SyllableType),
                    3: Q(syllable_types__endswith=SyllableType),
                    }
                    q_list_token.append( switcher.get(SyllableTypeSelect, "Invalid"))
            max_word_absolute= form.cleaned_data['max_word_absolute']
            if max_word_absolute>0:
                q_list_token.append( Q(chl_type_abs__lte=max_word_absolute))
            min_word_absolute= form.cleaned_data['min_word_absolute']
            if min_word_absolute>0:
                q_list_token.append( Q(chl_type_abs__gte=min_word_absolute))
            max_word_freq= form.cleaned_data['max_word_freq']
            if max_word_freq>0:
                q_list_token.append( Q(chl_type_norm__lte=max_word_freq))
            min_word_freq= form.cleaned_data['min_word_freq']
            if min_word_freq>0:
                q_list_token.append( Q(chl_type_norm__gte=min_word_freq))

            max_word_bigram= form.cleaned_data['max_word_bigram']
            if max_word_bigram>0:
                q_list_token.append( Q(chl_bigram_sum__lte=max_word_bigram))
            min_word_bigram= form.cleaned_data['min_word_bigram']
            if min_word_bigram>0:
                q_list_token.append( Q(chl_bigram_sum__gte=min_word_bigram))
            
            max_word_neighbors= form.cleaned_data['max_word_neighbors']
            if max_word_neighbors>0:
                q_list_token.append( Q(chl_nein__lte=max_word_neighbors))
            min_word_neighbors= form.cleaned_data['min_word_neighbors']
            if min_word_neighbors>0:
                q_list_token.append( Q(chl_nein__gte=min_word_neighbors))

            max_word_OLD20= form.cleaned_data['max_word_OLD20']
            if max_word_OLD20>0:
                q_list_token.append( Q(chl_nei_old20__lte=max_word_OLD20))
            min_word_OLD20= form.cleaned_data['min_word_OLD20']
            if min_word_OLD20>0:
                q_list_token.append( Q(chl_nei_old20__gte=min_word_OLD20))


            ErrorLevel= form.cleaned_data['ErrorLevel']
            ErrorLevelSelected= form.cleaned_data['ErrorLevelSelected']
            KOF= form.cleaned_data['KOF']
            ErrorKOFSelected= form.cleaned_data['ErrorKOFSelected']
            ErrorKOF= form.cleaned_data['ErrorKOF']
            resultmodel=models.Tbltokenbase.objects.filter(reduce(operator.and_, q_list_token))

    else:
        form=SearchViewModel.SearchItem()
            
           
            

 
    minmaxmodel=SearchViewModel.MinMaxSearchValue()
    max_no_phonemes=models.Tbltokenbase.objects.aggregate(maxph=Max('no_phonemes'))['maxph']
    min_no_phonemes=models.Tbltokenbase.objects.aggregate(minph=Min('no_phonemes'))['minph']
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
    datacount=SearchViewModel.DataCount()
    datacount.observations  = models.Tbltokenbase.objects.count()
    datacount.students  = models.Students.objects.count()
    datacount.wordforms  = models.Tbltypebase.objects.count()
    datacount.texts  = models.Tbltokenbase.objects.values('text_id').distinct().count()
    datacount.lemmas  = models.Tbltokenbase.objects.exclude(chl_lemma__isnull=True).values('chl_lemma').distinct().count()
    
 
    
    

    context={'form': form,'result':resultmodel,
    'maxminModel':minmaxmodel,
    'fields' :Tbltokenbase._meta.get_fields(),
    'datacount':datacount
    }
    return render(request, "MainSearch.Html", context)

 