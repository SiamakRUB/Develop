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
    q_list_Student=[]
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

            # max_Err_wordform= form.cleaned_data['max_Err_wordform']
            # if max_Err_wordform>0:
            #     q_list_token.append( Q(perc_erroneous__lte=max_Err_wordform))
            # min_Err_wordform= form.cleaned_data['max_Err_wordform']
            # if min_Err_wordform>0:
            #     q_list_token.append( Q(perc_erroneous__gte=min_Err_wordform))    
            
            max_Err_child= form.cleaned_data['max_Err_child']
            if max_Err_child>0:
                q_list_token.append( Q(erroneous__lte=max_Err_child))
            min_Err_child= form.cleaned_data['min_Err_child']
            if min_Err_child>0:
                q_list_token.append( Q(erroneous__gte=min_Err_child))  

            ErrorLevel= form.cleaned_data['ErrorLevel']
            ErrorLevelSelected= form.cleaned_data['ErrorLevelSelected']
            KOF= form.cleaned_data['KOF']
            ErrorKOFSelected= form.cleaned_data['ErrorKOFSelected']
            ErrorKOF= form.cleaned_data['ErrorKOF']

            StudentSex= form.cleaned_data['StudentSex']
            if StudentSex>0:
                switcher = {
                    1: Q(Geschl='w'),
                    2: Q(Geschl='m'),
                    3: Q(Geschl='k.A.')
                }
                q_list_Student.append(switcher.get(StudentSex, "Invalid") )  

            StudentNativecountry= form.cleaned_data['StudentNativecountry']
            if StudentNativecountry>0:
                switcher = {
                    1: Q(HLKLI='Deutschland'),
                    2: Q(HLKLI='nicht Deutschland'),
                    3: Q(HLKLI='k.A.')
                }
                q_list_Student.append(switcher.get(StudentNativecountry, "Invalid") )  

            Multilingual= form.cleaned_data['Multilingual']
            if Multilingual>0:
                switcher = {
                    1: Q(HLKLI='ja'),
                    2: Q(HLKLI='nein'),
                    3: Q(HLKLI='k.A.')
                }
                q_list_Student.append(switcher.get(Multilingual, "Invalid") )
            StudentPreferredReading= form.cleaned_data['StudentPreferredReading']
            if StudentPreferredReading>0:
                switcher = {
                    1: Q(SprechS='Deutsch'),
                    2: ~Q(SprechS='Deutsch'),
                    3: Q(SprechS='Muttersprache'),
                    4: Q(SprechS='k.A.')
                }
                q_list_Student.append(switcher.get(StudentPreferredReading, "Invalid") )

            StudentPreferredSpeaking= form.cleaned_data['StudentPreferredSpeaking']
            if StudentPreferredSpeaking>0:
                switcher = {
                    1: Q(SprechS='Deutsch'),
                    2: ~Q(SprechS='Deutsch'),
                    3: Q(SprechS='k.A.')
                }
                q_list_Student.append(switcher.get(StudentPreferredSpeaking, "Invalid") )
            
            StudentTeachingGerman= form.cleaned_data['StudentTeachingGerman']
            if StudentTeachingGerman>0:
                switcher = {
                    1: Q(DaZu='ja'),
                    2: Q(DaZu='nein'),
                    3: Q(DaZu='k.A.')
                }
                q_list_Student.append(switcher.get(StudentTeachingGerman, "Invalid") )  
            
            StudentTeachingNative= form.cleaned_data['StudentTeachingNative']
            if StudentTeachingNative>0:
                switcher = {
                    1: Q(mu_hsu='ja'),
                    2: Q(mu_hsu='nein'),
                    3: Q(mu_hsu='k.A.')
                }
                q_list_Student.append(switcher.get(StudentTeachingNative, "Invalid") )  
            
            max_student_writing= form.cleaned_data['max_student_writing']
            if max_student_writing>0:
                q_list_Student.append( Q(anzahl__lte=max_student_writing))  
            
            min_student_writing= form.cleaned_data['min_student_writing']
            if min_student_writing>0:
                q_list_Student.append( Q(anzahl__gte=min_student_writing))  


            StudentOriginFather= form.cleaned_data['StudentOriginFather']
            if StudentOriginFather>0:
                switcher = {
                    1: Q(hsprvli='Deutsch'),
                    2: ~Q(hsprvli='Deutsch'),
                    3: Q(hsprvli='k.A.')
                }
                q_list_Student.append(switcher.get(StudentOriginFather, "Invalid") )    
            
            
            StudentOriginMother= form.cleaned_data['StudentOriginMother']
            if StudentOriginMother>0:
                switcher = {
                    1: Q(hsprmli='Deutsch'),
                    2: ~Q(hsprmli='Deutsch'),
                    3: Q(hsprmli='k.A.')
                }
                q_list_Student.append(switcher.get(StudentOriginMother, "Invalid") )  

            
            StudentcountryFather= form.cleaned_data['StudentcountryFather']
            if StudentcountryFather>0:
                switcher = {
                    1: Q(hlvli='Deutschland'),
                    2: ~Q(hlvli='Deutschland'),
                    3: Q(hlvli='k.A.')
                }
                q_list_Student.append(switcher.get(StudentcountryFather, "Invalid") )  

            
            StudentcountryMother= form.cleaned_data['StudentcountryMother']
            if StudentcountryMother>0:
                switcher = {
                    1: Q(hlmli='Deutschland'),
                    2: ~Q(hlmli='Deutschland'),
                    3: Q(hlmli='k.A.')
                }
                q_list_Student.append(switcher.get(StudentcountryMother, "Invalid") ) 

            # StudentTestTimeSelect= form.cleaned_data['StudentTestTimeSelect']
            # if StudentTestTimeSelect>0:
            #     q_list_token.append( Q(erroneous__gte=StudentTestTimeSelect))
            
            # StudentStorySelect= form.cleaned_data['StudentStorySelect']
            # if StudentStorySelect>0:
            #     q_list_token.append( Q(erroneous__gte=StudentStorySelect))
            
            # StudentStory= form.cleaned_data['StudentStory']
            # if StudentStory>0:
            #     q_list_token.append( Q(erroneous__gte=StudentStory))

            # StudentTestTimeSelect= form.cleaned_data['StudentTestTimeSelect']
            # if StudentTestTimeSelect>0:
            #     q_list_token.append( Q(erroneous__gte=StudentTestTimeSelect))
            DonchartModel= SearchViewModel().DataCount()
            storylist=models.Tbltokenbase.objects.distinct('story')
            # DonchartModel.storycat.append()
            resultmodel=models.Tbltokenbase.objects.filter(reduce(operator.and_, q_list_token))
           



    else:
        form=SearchViewModel.SearchItem()

            
           
            

 
    minmaxmodel=SearchViewModel.MinMaxSearchValue()
    tbltoken=models.Tbltokenbase.objects
    tbltype=models.Tbltypebase.objects
    max_no_phonemes=tbltoken.aggregate(maxph=Max('no_phonemes'))['maxph']
    min_no_phonemes=tbltoken.aggregate(minph=Min('no_phonemes'))['minph']
    max_norm=tbltype.aggregate(norm=Max('chl_lemma_norm'))['norm']
    min_norm=tbltype.aggregate(norm=Min('chl_lemma_norm'))['norm']
    max_abs=tbltype.aggregate(abs=Max('chl_lemma_abs'))['abs']
    min_abs=tbltype.aggregate(abs=Min('chl_lemma_abs'))['abs']
    max_lemmazipf=tbltype.aggregate(abs=Max('lemma_zipf'))['abs']
    min_lemmazipf=tbltype.aggregate(abs=Min('lemma_zipf'))['abs']

    minmaxmodel.max_norm=max_norm
    minmaxmodel.min_norm=min_norm
    minmaxmodel.max_abs=max_abs
    minmaxmodel.min_abs=min_abs
    minmaxmodel.max_lemmazipf=max_lemmazipf
    minmaxmodel.min_lemmazipf=min_lemmazipf
    minmaxmodel.max_no_phonemes=max_no_phonemes
    minmaxmodel.min_no_phonemes=min_no_phonemes

 
    max_no_graphemes=tbltype.aggregate(maxph=Max('no_graphemes'))['maxph']
    min_no_graphemes=tbltype.aggregate(minph=Min('no_graphemes'))['minph']
    max_no_syllables=tbltype.aggregate(norm=Max('no_syllables'))['norm']
    min_no_syllables=tbltype.aggregate(norm=Min('no_syllables'))['norm']
    max_no_morphemes=tbltype.aggregate(abs=Max('no_morphemes'))['abs']
    min_no_morphemes=tbltype.aggregate(abs=Min('no_morphemes'))['abs']
    max_chl_type_abs=tbltype.aggregate(abs=Max('chl_type_abs'))['abs']
    min_chl_type_abs=tbltype.aggregate(abs=Min('chl_type_abs'))['abs']
    
    minmaxmodel.max_no_graphemes=max_no_graphemes
    minmaxmodel.min_no_graphemes=min_no_graphemes
    minmaxmodel.max_no_syllables=max_no_syllables
    minmaxmodel.min_no_syllables=min_no_syllables
    minmaxmodel.max_no_morphemes=max_no_morphemes
    minmaxmodel.min_no_morphemes=min_no_morphemes
    minmaxmodel.max_chl_type_abs=max_chl_type_abs
    minmaxmodel.min_chl_type_abs=min_chl_type_abs

    max_chl_type_norm=tbltype.aggregate(maxph=Max('chl_type_norm'))['maxph']
    min_chl_type_norm=tbltype.aggregate(minph=Min('chl_type_norm'))['minph']
    max_chl_bigram_sum=tbltype.aggregate(norm=Max('chl_bigram_sum'))['norm']
    min_chl_bigram_sum=tbltype.aggregate(norm=Min('chl_bigram_sum'))['norm']
    max_chl_nei_n=tbltype.aggregate(abs=Max('chl_nei_n'))['abs']
    min_chl_nei_n=tbltype.aggregate(abs=Min('chl_nei_n'))['abs']
    max_chl_nei_OLD20=tbltoken.aggregate(abs=Max('chl_nei_old20'))['abs']
    min_chl_nei_OLD20=tbltoken.aggregate(abs=Min('chl_nei_old20'))['abs']

    minmaxmodel.max_chl_type_norm=max_chl_type_norm
    minmaxmodel.min_chl_type_norm=min_chl_type_norm
    minmaxmodel.max_chl_bigram_sum=max_chl_bigram_sum
    minmaxmodel.min_chl_bigram_sum=min_chl_bigram_sum
    minmaxmodel.max_chl_nei_n=max_chl_nei_n
    minmaxmodel.min_chl_nei_n=min_chl_nei_n
    minmaxmodel.max_chl_nei_OLD20=max_chl_nei_OLD20
    minmaxmodel.min_chl_nei_OLD20=min_chl_nei_OLD20

    min_Err_wordform=tbltype.aggregate(abs=Min('perc_erroneous'))['abs']
    max_Err_wordform=tbltype.aggregate(abs=Max('perc_erroneous'))['abs']

    minmaxmodel.min_Err_wordform=min_Err_wordform
    minmaxmodel.max_Err_wordform=max_Err_wordform
    # min_Err_child=tbltoken.filter(target=orig).aggregate(abs=Max('chl_nei_old20'))['abs']
    # max_Err_child=tbltoken.aggregate(abs=Min('chl_nei_old20'))['abs']
    min_Err_child=tbltoken.aggregate(abs=Min('erroneous'))['abs']
    max_Err_child=tbltoken.aggregate(abs=Max('erroneous'))['abs']
    minmaxmodel.min_Err_child=min_Err_child
    minmaxmodel.max_Err_child=max_Err_child
    
    # no_graphemes
    # no_syllables
    # no_morphemes
    # chl_type.abs
    # chl_type.norm
    # chl_bigram.sum
    # chl_nei.n
    # chl_nei.OLD20
    datacount=SearchViewModel.DataCount()
    datacount.observations  = tbltoken.count()
    datacount.students  = models.Students.objects.count()
    datacount.wordforms  = tbltype.count()
    datacount.texts  = tbltoken.values('text_id').distinct().count()
    datacount.lemmas  = tbltoken.exclude(chl_lemma__isnull=True).values('chl_lemma').distinct().count()
    stdids=models.Students.objects.only('number')
    #  [1,2,3,4]
 
    
    

    context={'form': form,'result':resultmodel,
    'maxminModel':minmaxmodel,
    'fields' :Tbltokenbase._meta.get_fields(),
    'datacount':datacount,
    'stdids':stdids,
    }
    return render(request, "MainSearch.Html", context)

 