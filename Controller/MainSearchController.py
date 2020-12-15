from django.shortcuts import render
from django.http import HttpResponse
from RubLitKeyService import models
from ModelViews import SearchViewModel
from django.db.models import Max
from django.db.models import Min
from django.db.models import Q
from functools import reduce
from RubLitKeyService.models import Tbltokenbase
from django.db import connection
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt 
import operator
# def getindexOfString(strvalue,mylist):
#     indices = [i for i, s in enumerate(mylist) if strvalue in s]
#     return indices
# def switchStoryIndex(selectedvalue):  
#     switcher = {
#         0:"Eis",
#         1:"Weg_2",
#         2:"Frosch",
#         3:"Jenga",
#         4:"Staubsauger",
#         5:"Weg_3",
#         6:"Schule",
#         7:"Fundbuero",
#         8:"Seilbahn",
#         9: "Weg_4",
#     }
#     func= switcher.get(selectedvalue, "Invalid")
#     return func()
def multiselectAsList(strval):
        return strval.split(',')

def switchStringSelect(selectedvalue):  
    switcher = {
        1: "startswith",
        2: "contains",
        3: "endswith",
    }
    func= switcher.get(selectedvalue, "Invalid")
    return func()
def get_Token_Student_sql(textids ):
    my_string = "','".join(textids) 
    cursor = connection.cursor()    
    strcommand="SELECT * FROM tbltokenbase as tk left JOIN students as st on st.t1=tk.text_id or st.T2=tk.text_id or st.T3=tk.text_id or st.T4=tk.text_id or st.T5=tk.text_id or st.T6=tk.text_id or st.T7=tk.text_id or st.T8=tk.text_id or st.T9=tk.text_id or st.T10=tk.text_id   where tk.text_id IN ('"+my_string+"')"
    cursor.execute(strcommand )
    row = cursor.fetchone()
    return row
def MaxMinSliderLoad(minmaxmodel):  
   
    max_no_phonemes=21#tbltoken.aggregate(maxph=Max('no_phonemes'))['maxph']
    min_no_phonemes=0#tbltoken.aggregate(minph=Min('no_phonemes'))['minph']
    max_norm=106056.033#tbltype.aggregate(norm=Max('chl_lemma_norm'))['norm']
    min_norm=0#tbltype.aggregate(norm=Min('chl_lemma_norm'))['norm']
    max_abs=782243#tbltype.aggregate(abs=Max('chl_lemma_abs'))['abs']
    min_abs=0#tbltype.aggregate(abs=Min('chl_lemma_abs'))['abs']
    max_lemmazipf=8.026#tbltype.aggregate(abs=Max('lemma_zipf'))['abs']
    min_lemmazipf=0#tbltype.aggregate(abs=Min('lemma_zipf'))['abs']

    minmaxmodel.max_norm=max_norm
    minmaxmodel.min_norm=min_norm
    minmaxmodel.max_abs=max_abs
    minmaxmodel.min_abs=min_abs
    minmaxmodel.max_lemmazipf=max_lemmazipf
    minmaxmodel.min_lemmazipf=min_lemmazipf
    minmaxmodel.max_no_phonemes=max_no_phonemes
    minmaxmodel.min_no_phonemes=min_no_phonemes


    max_no_graphemes=22#tbltype.aggregate(maxph=Max('no_graphemes'))['maxph']
    min_no_graphemes=1#tbltype.aggregate(minph=Min('no_graphemes'))['minph']
    max_no_syllables=8#tbltype.aggregate(norm=Max('no_syllables'))['norm']
    min_no_syllables=0#tbltype.aggregate(norm=Min('no_syllables'))['norm']
    max_no_morphemes=9#tbltype.aggregate(abs=Max('no_morphemes'))['abs']
    min_no_morphemes=1#tbltype.aggregate(abs=Min('no_morphemes'))['abs']
    max_chl_type_abs=212632#tbltype.aggregate(abs=Max('chl_type_abs'))['abs']
    min_chl_type_abs=0#tbltype.aggregate(abs=Min('chl_type_abs'))['abs']
    
    minmaxmodel.max_no_graphemes=max_no_graphemes
    minmaxmodel.min_no_graphemes=min_no_graphemes
    minmaxmodel.max_no_syllables=max_no_syllables
    minmaxmodel.min_no_syllables=min_no_syllables
    minmaxmodel.max_no_morphemes=max_no_morphemes
    minmaxmodel.min_no_morphemes=min_no_morphemes
    minmaxmodel.max_chl_type_abs=max_chl_type_abs
    minmaxmodel.min_chl_type_abs=min_chl_type_abs

    max_chl_type_norm=28828.518#tbltype.aggregate(maxph=Max('chl_type_norm'))['maxph']
    min_chl_type_norm=0#tbltype.aggregate(minph=Min('chl_type_norm'))['minph']
    max_chl_bigram_sum=464498#tbltype.aggregate(norm=Max('chl_bigram_sum'))['norm']
    min_chl_bigram_sum=0#tbltype.aggregate(norm=Min('chl_bigram_sum'))['norm']
    max_chl_nei_n=22#tbltype.aggregate(abs=Max('chl_nei_n'))['abs']
    min_chl_nei_n=0#tbltype.aggregate(abs=Min('chl_nei_n'))['abs']
    max_chl_nei_OLD20=7.2#tbltoken.aggregate(abs=Max('chl_nei_old20'))['abs']
    min_chl_nei_OLD20=0#tbltoken.aggregate(abs=Min('chl_nei_old20'))['abs']

    minmaxmodel.max_chl_type_norm=max_chl_type_norm
    minmaxmodel.min_chl_type_norm=min_chl_type_norm
    minmaxmodel.max_chl_bigram_sum=max_chl_bigram_sum
    minmaxmodel.min_chl_bigram_sum=min_chl_bigram_sum
    minmaxmodel.max_chl_nei_n=max_chl_nei_n
    minmaxmodel.min_chl_nei_n=min_chl_nei_n
    minmaxmodel.max_chl_nei_OLD20=max_chl_nei_OLD20
    minmaxmodel.min_chl_nei_OLD20=min_chl_nei_OLD20

    min_Err_wordform=0#tbltype.aggregate(abs=Min('perc_erroneous'))['abs']
    max_Err_wordform=100#tbltype.aggregate(abs=Max('perc_erroneous'))['abs']

    minmaxmodel.min_Err_wordform=min_Err_wordform
    minmaxmodel.max_Err_wordform=max_Err_wordform
    # min_Err_child=tbltoken.filter(target=orig).aggregate(abs=Max('chl_nei_old20'))['abs']
    # max_Err_child=tbltoken.aggregate(abs=Min('chl_nei_old20'))['abs']
    min_Err_child=0#tbltoken.aggregate(abs=Min('erroneous'))['abs']
    max_Err_child=1#tbltoken.aggregate(abs=Max('erroneous'))['abs']
    minmaxmodel.min_Err_child=min_Err_child
    minmaxmodel.max_Err_child=max_Err_child
    minmaxmodel.max_student_writing=10
    minmaxmodel.min_student_writing=0
    return minmaxmodel

@csrf_exempt
def ShowGroupSetting(request ):
    if request.method == 'POST':
        showCols1 = request.POST.getlist('showcols[]', None) 
        showfieldsLabel1 = request.POST.getlist('showfieldsLabel[]', None) 
    
        request.session['Showing'] = showCols1
        request.session['showfieldsLabel'] = showfieldsLabel1
    
    return JsonResponse({'success':False, 'errorMsg':"test",'data':showCols1,'datalbl':showfieldsLabel1})


def MainSearch (request) :
   
    StudentIDSelected=""
    inp_target=""
    storyTypevalues=[] 
    storyTypeLabel=[]


    storyPosvalues=[] 
    storyPosLabel=[] 

    storyErrorvalues=[] 
    storyErrorLabel=[] 

    storyOrigvalues=[] 
    storyOrigLabel=[] 
    showpanel='hide'


    ShowCols=["chl_lemma","chl_lemma_norm","chl_lemma_abs","lemma_zipf","target","orig","no_phonemes",
    "no_graphemes","no_syllables","no_morphemes","POS",
    "syllable_types","chl_type_abs","chl_type_norm","chl_bigram_sum",
    "chl_nein","chl_nei_old20","error_level"]#default grid col names
    ShowfieldsLabel=["Lemma","Lemma freq per 1M","Lemma absolute freq","Zipf score","wordform","original","no phonemes",
    "no graphemes","no syllables","no morphemes", "POS",
    "syllable types " ,
    "absolute freq","word freq per 1M","summed bigram freq","no. neighbors","OLD20","Error level"]
    if 'Showing' in request.session:
        fieldsselected=request.session['Showing'] 
        if fieldsselected :
            ShowCols = request.session['Showing']# default query set fields
    if 'showfieldsLabel' in request.session:
        fieldsselected=request.session['showfieldsLabel']
        if fieldsselected :
            ShowfieldsLabel= request.session['showfieldsLabel'] 

    resultmodel=[]
    #models.Tbltokenbase.objects.filter(id__lte=0)
    testmodel=[]
    #models.Tbltokenbase.objects.filter(id__lte=0)

    DonchartModel= SearchViewModel.ChartDonat()
    ChartBarNumberWord= SearchViewModel.ChartBarNumberWord()
    ChartStoryDeveloped= SearchViewModel.ChartStoryDeveloped()
    # ShowColumnsModel= SearchViewModel.ShowColumnGrid()
    tbltoken=models.Tbltokenbase.objects
    tbltype=models.Tbltypebase.objects
    my_string=""
    strcommand=""
    textids=[]
    # x=get_Token_Student_sql(['029-200910-I-Eis', '065-200910-I-Eis','026-201011-II-Jenga', '161-201011-II-Jenga','04-237-3-II-Jenga', '095-201011-IV-Weg', '080-201011-I-Schule', '080-201011-I-Schule', '117-201011-I-Schule','132-201112-I-Schule','150-201011-I-Schule', '07-211-4-I-Schule', '07-329-4-I-Schule', '07-382-4-I-Schule', '07-390-4-I-Schule', '07-476-4-I-Schule', '07-489-4-I-Schule', '07-620-4-I-Schule', '07-622-4-I-Schule','07-622-4-I-Schule'])
    Token_Student=[]
    AggregatedLema=[]
    AggregatedText=[]
    AggregatedGlobal=[]
    ChartAge=[]
    ChartAgeType=[]
    ListOfShowFields=[]


    AverageTokenStoryMultilanguage=[]
    AverageTokenStoryGerman=[]
    AverageTokenStoryNA=[]

    ListFilterItems =[]
    q_list_type =[]
    q_list_token=[] 
    q_list_Student=[]
    if  request.method == "POST":
        form = SearchViewModel.SearchItem(request.POST)
        if form.is_valid():
            showpanel=''
            LemmaSelect= int(form.cleaned_data['LemmaSelect'])
            Lemma= form.cleaned_data['Lemma']
            # ShowColumnsModel.Showlemma=bool(form.cleaned_data['Showlemma'])
            # if ShowColumnsModel.Showlemma:
            #     ListOfShowFields.append("chl_lemma")

            # ShowColumnsModel.Showlemmaabsolutefreq=bool(form.cleaned_data['Showlemmaabsolutefreq'])
            # if ShowColumnsModel.Showlemmaabsolutefreq:
            #     ListOfShowFields.append("chl_lemma_abs")
            # ShowColumnsModel.Showlemmafreqper1M=bool(form.cleaned_data['Showlemmafreqper1M'])
            # if ShowColumnsModel.Showlemmafreqper1M:
            #     ListOfShowFields.append("chl_lemma_norm")
            # ShowColumnsModel.ShowlemmaZipfscore=bool(form.cleaned_data['ShowlemmaZipfscore'])
            # if ShowColumnsModel.ShowlemmaZipfscore:
            #     ListOfShowFields.append("lemma_zipf") 
            
            if Lemma:
                if LemmaSelect>-1:
                    switcher = {
                    0: Q(chl_lemma=Lemma),
                    1: Q(chl_lemma__startswith=Lemma),
                    2: Q(chl_lemma__contains=Lemma),
                    3: Q(chl_lemma__endswith=Lemma),
                    }
                    ListFilterItems.append("Lema :{} ".format(Lemma))

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
                    ListFilterItems.append("Orig:{} ".format(Orig))
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
                    ListFilterItems.append("Target: {}".format(Target))
                    q_list_token.append( switcher.get(TargetSelect, "Invalid"))

            # IsFunktion= form.cleaned_data['IsFunktion']
            # IsLexion= form.cleaned_data['IsLexion']

            POSSelect= int(form.cleaned_data['POSSelect'])  
            POS=str( form.cleaned_data['POS'])
            if POS:
                if POSSelect>-1:
                    switcher = {
                    0: Q(pos=POS),
                    1: Q(pos__istartswith=POS),
                    2: Q(pos__icontains=POS),
                    3: Q(pos__iendswith=POS),
                    }
                    q_list_token.append( switcher.get(POSSelect, "Invalid"))
                    ListFilterItems.append("POS: {}".format(POS))
            
           

            max_lemma_freq= form.cleaned_data['max_lemma_freq']
            if max_lemma_freq>0:
                q_list_token.append( Q(chl_lemma_norm__lte=max_lemma_freq))
                ListFilterItems.append(" max lemma freq: {}".format(max_lemma_freq))
            min_lemma_freq= form.cleaned_data['min_lemma_freq']
            if min_lemma_freq>0:
                ListFilterItems.append(" min lemma_freq: {}".format(min_lemma_freq))
                q_list_token.append( Q(chl_lemma_norm__gte=min_lemma_freq))
            

            max_lemma_absolute= form.cleaned_data['max_lemma_absolute']
            if max_lemma_absolute>0:
                ListFilterItems.append(" max lemma freq abs: {}".format(max_lemma_absolute))
                q_list_token.append( Q(chl_lemma_abs__lte=max_lemma_absolute))

            min_lemma_absolute= form.cleaned_data['min_lemma_absolute']
            if min_lemma_absolute>0:
                ListFilterItems.append(" min lemma freq abs: {}".format(min_lemma_absolute))
                q_list_token.append( Q(chl_lemma_abs__gte=min_lemma_freq))

            max_lemma_Zipf= form.cleaned_data['max_lemma_Zipf']
            if max_lemma_Zipf>0:
                ListFilterItems.append(" max lemma Zipf: {}".format(max_lemma_Zipf))
                q_list_token.append( Q(lemma_zipf__lte=max_lemma_Zipf))

            min_lemma_Zipf= form.cleaned_data['min_lemma_Zipf']
            if min_lemma_Zipf>0:
                ListFilterItems.append(" min lemma Zipf: {}".format(min_lemma_Zipf))
                q_list_token.append( Q(lemma_zipf__gte=min_lemma_Zipf))

            max_word_phonemes= form.cleaned_data['max_word_phonemes']
            if max_word_phonemes>0:
                ListFilterItems.append(" max word phonemes: {}".format(max_word_phonemes))
                q_list_token.append( Q(no_phonemes__lte=max_word_phonemes))
            
        #    ///
            min_word_phonemes= form.cleaned_data['min_word_phonemes']
            if min_word_phonemes>0:
                ListFilterItems.append(" min word phonemes: {}".format(min_word_phonemes))
                q_list_token.append( Q(no_phonemes__gte=min_word_phonemes))
            
            max_word_graphemes= form.cleaned_data['max_word_graphemes']
            if max_word_graphemes>0:
                ListFilterItems.append(" max word graphemes: {}".format(max_word_graphemes))
                q_list_token.append( Q(no_graphemes__lte=max_word_graphemes))
            min_word_graphemes= form.cleaned_data['min_word_graphemes']
            if min_word_graphemes>0:
                ListFilterItems.append("min word graphemes: {}".format(min_word_graphemes))
                q_list_token.append( Q(no_graphemes__gte=min_word_graphemes))

            max_word_syllables= form.cleaned_data['max_word_syllables']
            if max_word_syllables>0:
                ListFilterItems.append("max word syllables: {}".format(max_word_syllables))
                q_list_token.append( Q(no_syllables__lte=max_word_syllables))
            min_word_syllables= form.cleaned_data['min_word_syllables']
            if min_word_syllables>0:
                ListFilterItems.append("min word syllables: {}".format(min_word_syllables))
                q_list_token.append( Q(no_syllables__gte=min_word_syllables))

            max_word_morphemes= form.cleaned_data['max_word_morphemes']
            if max_word_morphemes>0:
                ListFilterItems.append(" max word morphemes: {}".format(max_word_morphemes))
                q_list_token.append( Q(no_morphemes__lte=max_word_morphemes))
            min_word_morphemes= form.cleaned_data['min_word_morphemes']
            if min_word_morphemes>0:
                ListFilterItems.append("min word morphemes: {}".format(min_word_morphemes))
                q_list_token.append( Q(no_morphemes__gte=min_word_morphemes))
           
            SyllableTypeSelect= form.cleaned_data['SyllableTypeSelect']
            SyllableType= form.cleaned_data['SyllableType']
            if SyllableType:
                if SyllableTypeSelect>-1:
                    switcher = {
                    0: Q(syllable_types=SyllableType),
                    1: Q(syllable_types__istartswith=SyllableType),
                    2: Q(syllable_types__icontains=SyllableType),
                    3: Q(syllable_types__iendswith=SyllableType),
                    }
                    ListFilterItems.append("SyllableType: {}".format(SyllableType))
                    q_list_token.append( switcher.get(SyllableTypeSelect, "Invalid"))
            max_word_absolute= form.cleaned_data['max_word_absolute']
            if max_word_absolute>0:
                ListFilterItems.append("max word absolute: {}".format(max_word_absolute))
                q_list_token.append( Q(chl_type_abs__lte=max_word_absolute))
            min_word_absolute= form.cleaned_data['min_word_absolute']
            if min_word_absolute>0:
                ListFilterItems.append("min word absolute: {}".format(min_word_absolute))
                q_list_token.append( Q(chl_type_abs__gte=min_word_absolute))
            max_word_freq= form.cleaned_data['max_word_freq']
            if max_word_freq>0:
                ListFilterItems.append("max word freq: {}".format(max_word_freq))
                q_list_token.append( Q(chl_type_norm__lte=max_word_freq))
            min_word_freq= form.cleaned_data['min_word_freq']
            if min_word_freq>0:
                ListFilterItems.append("min word freq: {}".format(min_word_freq))
                q_list_token.append( Q(chl_type_norm__gte=min_word_freq))

            max_word_bigram= form.cleaned_data['max_word_bigram']
            if max_word_bigram>0:
                ListFilterItems.append("max word bigram: {}".format(max_word_bigram))
                q_list_token.append( Q(chl_bigram_sum__lte=max_word_bigram))
            min_word_bigram= form.cleaned_data['min_word_bigram']
            if min_word_bigram>0:
                ListFilterItems.append("min word bigram: {}".format(min_word_bigram))
                q_list_token.append( Q(chl_bigram_sum__gte=min_word_bigram))
            
            max_word_neighbors= form.cleaned_data['max_word_neighbors']
            if max_word_neighbors>0:
                ListFilterItems.append("max word neighbors: {}".format(max_word_neighbors))
                q_list_token.append( Q(chl_nein__lte=max_word_neighbors))
            min_word_neighbors= form.cleaned_data['min_word_neighbors']
            if min_word_neighbors>0:
                ListFilterItems.append("min word neighbors: {}".format(min_word_neighbors))
                q_list_token.append( Q(chl_nein__gte=min_word_neighbors))

            max_word_OLD20= form.cleaned_data['max_word_OLD20']
            if max_word_OLD20>0:
                ListFilterItems.append("max word OLD20: {}".format(max_word_OLD20))
                q_list_token.append( Q(chl_nei_old20__lte=max_word_OLD20))
            min_word_OLD20= form.cleaned_data['min_word_OLD20']
            if min_word_OLD20>0:
                ListFilterItems.append("min word OLD20: {}".format(min_word_OLD20))
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



            StudentSex= form.cleaned_data['StudentSex']
            if StudentSex>0:
                # switcher = {
                #     1: Q(Geschl='w'),
                #     2: Q(Geschl='m'),
                #     3: Q(Geschl='k.A.')
                # }
                switcher = {
                    1: "Geschl='w' " ,
                    2: "Geschl='m' ",
                    3: "Geschl='k.A.' "

                }
                # q_list_Student.append(switcher.get(StudentSex, "Invalid") )  
                ListFilterItems.append("Student Sex: {}".format(StudentSex))
                q_list_Student.append(switcher.get(StudentSex, "Invalid") )  

            StudentNativecountry= form.cleaned_data['StudentNativecountry']
            if StudentNativecountry>0:
                # switcher = {
                #     1: Q(HLKLI='Deutschland'),
                #     2: Q(HLKLI='nicht Deutschland'),
                #     3: Q(HLKLI='k.A.')
                # }
                switcher = {
                    1: "HLKLI='Deutschland' ",
                    2: "HLKLI='nicht Deutschland' ",
                    3: "HLKLI='k.A.' "
                }
                ListFilterItems.append("Nativecountry: {}".format(StudentNativecountry))
                q_list_Student.append(switcher.get(StudentNativecountry, " ") )  

            Multilingual= form.cleaned_data['Multilingual']
            if Multilingual>0:
                # switcher = {
                #     1: Q(HLKLI='ja'),
                #     2: Q(HLKLI='nein'),
                #     3: Q(HLKLI='k.A.')
                # }
                switcher = {
                    1: " multilingual='ja' ",
                    2: " multilingual='nein' ",
                    3: " multilingual='k.A.' "
                }
                ListFilterItems.append("Multilingual: {}".format(StudentNativecountry))
                q_list_Student.append(switcher.get(Multilingual, " ") )

            StudentPreferredReading= form.cleaned_data['StudentPreferredReading']
            if StudentPreferredReading>0:
                # switcher = {
                #     1: Q(LesS='Deutsch'),
                #     2: ~Q(LesS='Deutsch'),
                #     3: Q(LesS='Muttersprache'),
                #     4: Q(LesS='k.A.')
                # }
                switcher = {
                    1: "LesS='Deutsch' ",
                    2: "LesS<>'Deutsch' ",
                    3: "LesS='Muttersprache' ",
                    4: "LesS='k.A.' "
                }
                ListFilterItems.append("Preferred Reading: {}".format(StudentPreferredReading))
                q_list_Student.append(switcher.get(StudentPreferredReading, "") )

            StudentPreferredSpeaking= form.cleaned_data['StudentPreferredSpeaking']
            if StudentPreferredSpeaking>0:
                # switcher = {
                #     1: Q(SprechS='Deutsch'),
                #     2: ~Q(SprechS='Deutsch'),
                #     3: Q(SprechS='k.A.')
                # }
                switcher = {
                    1: "SprechS='Deutsch' ",
                    2: "SprechS<>'Deutsch' ",
                    3: "SprechS='k.A.' "
                }
                ListFilterItems.append("Preferred Speaking: {}".format(StudentPreferredSpeaking))
                q_list_Student.append(switcher.get(StudentPreferredSpeaking, "") )
            
            StudentTeachingGerman= form.cleaned_data['StudentTeachingGerman']
            if StudentTeachingGerman>0:
                # switcher = {
                #     1: Q(DaZu='ja'),
                #     2: Q(DaZu='nein'),
                #     3: Q(DaZu='k.A.')
                # }
                switcher = {
                    1: "DaZu='ja' ",
                    2: "DaZu='nein' ",
                    3: "DaZu='k.A.' "
                }

                ListFilterItems.append("Teaching German: {}".format(StudentTeachingGerman))
                q_list_Student.append(switcher.get(StudentTeachingGerman, " ") )  
            
            StudentTeachingNative= form.cleaned_data['StudentTeachingNative']
            if StudentTeachingNative>0:
                # switcher = { 
                #     1: Q(mu_hsu='ja'),
                #     2: Q(mu_hsu='nein'),
                #     3: Q(mu_hsu='k.A.')
                # }
                switcher = {
                    1:  " MU_HSU ='ja' ",
                    2:  " MU_HSU ='nein' ",
                    3:  " MU_HSU ='k.A.' "
                }
                ListFilterItems.append("Teaching Native: {}".format(StudentTeachingNative))
                q_list_Student.append(switcher.get(StudentTeachingNative, " ") )  
            
            max_student_writing= form.cleaned_data['max_student_writing']
            if max_student_writing>0:
                # q_list_Student.append( Q(anzahl__lte=max_student_writing))  
                ListFilterItems.append("max student writing: {}".format(max_student_writing))
                q_list_Student.append( " anzahl<={} ".format(max_student_writing))
            
            min_student_writing= form.cleaned_data['min_student_writing']
            if min_student_writing>0:
                # q_list_Student.append( Q(anzahl__gte=min_student_writing))  
                ListFilterItems.append("min student writing: {}".format(min_student_writing))
                q_list_Student.append( " anzahl>={} ".format(min_student_writing)) 



            StudentOriginFather= form.cleaned_data['StudentOriginFather']
            if StudentOriginFather>0:
                # switcher = {
                #     1: Q(hsprvli='Deutsch'),
                #     2: ~Q(hsprvli='Deutsch'),
                #     3: Q(hsprvli='k.A.')
                # }
                switcher = {
                    1: "hsprvli='Deutsch' ",
                    2: "hsprvli<>'Deutsch' ",
                    3: "hsprvli='k.A.' "
                }
                if StudentOriginFather==1:
                    strgetval= "German" 
                else:
                    strgetval="not German"
                ListFilterItems.append("Origin Father: {}".format(strgetval))
                q_list_Student.append(switcher.get(StudentOriginFather, " ") )    
            
            
            StudentOriginMother= form.cleaned_data['StudentOriginMother']
            if StudentOriginMother>0:
                # switcher = {
                #     1: Q(hsprmli='Deutsch'),
                #     2: ~Q(hsprmli='Deutsch'),
                #     3: Q(hsprmli='k.A.')
                # }
                switcher = {
                    1: "hsprmli='Deutsch' ",
                    2: "hsprmli<>'Deutsch' ",
                    3: "hsprmli='k.A.' "
                }
                if StudentOriginMother==1:
                    strgetval= "German" 
                else:
                    strgetval="not German" 
                ListFilterItems.append("Origin Mother: {}".format(strgetval))
                q_list_Student.append(switcher.get(StudentOriginMother, " ") )  

            
            StudentcountryFather= form.cleaned_data['StudentcountryFather']
            if StudentcountryFather>0:
                # switcher = {
                #     1: Q(hlvli='Deutschland'),
                #     2: ~Q(hlvli='Deutschland'),
                #     3: Q(hlvli='k.A.')
                # }
                switcher = {
                    1: "hlvli='Deutschland' ",
                    2: "hlvli<>'Deutschland' ",
                    3: "hlvli='k.A.' "
                }
                if StudentcountryFather==1:
                    strgetval= "German" 
                else:
                    strgetval="not German" 
                ListFilterItems.append("country Father: {}".format(strgetval))
                q_list_Student.append(switcher.get(StudentcountryFather, " ") )  

            
            StudentcountryMother= form.cleaned_data['StudentcountryMother']
            if StudentcountryMother>0:
                # switcher = {
                #     1: Q(hlmli='Deutschland'),
                #     2: ~Q(hlmli='Deutschland'),
                #     3: Q(hlmli='k.A.')
                # }
                switcher = {
                    1: "hlmli='Deutschland' ",
                    2: "hlmli<>'Deutschland' ",
                    3: "hlmli='k.A.' "
                }
                strgetval=""
                if StudentcountryMother==1:
                    strgetval= "German" 
                else:
                    strgetval="not German" 
                ListFilterItems.append("country Father: {}".format( strgetval ))
                q_list_Student.append(switcher.get(StudentcountryMother, " ") ) 

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
            # DonchartModel.storycat.append() 
            # groupfields=request.session['grouping']
            # Showing=request.session['grouping']
            if q_list_token and len(q_list_token)>0 :
                resultmodel=models.Tbltokenbase.objects.filter(reduce(operator.and_, q_list_token))
                testmodel=models.Tbltokenbase.objects.filter(reduce(operator.and_, q_list_token)).values_list("id", flat=True) 
            
            # testmodel=models.Tbltokenbase.objects.filter(reduce(operator.and_, q_list_token)).values('id') 
            #textids=list(testmodel) 
            
            stropr=""
            data = []
            student_where_string=" " 
            for item in testmodel: #list is your initial datas format as python list  
                data.append(item)
            token_where_string=" "
            if data and len(data):
                token_where_string = ",".join(str(v) for v in data)  
            if len(data)>0:
                stropr=" and "
                token_where_string=" tk.id IN({}) ".format(token_where_string)
            else:
                if len (q_list_token)>0 :
                    token_where_string= "1=0 "
                    stropr=" and "

                else :
                    token_where_string= " "
                    stropr=""
            if len(q_list_Student)>0:
                student_where_string = " and ".join(q_list_Student)  
                student_where_string=" {} {}" .format(stropr,student_where_string) 
                
                    
                
            
            

            # if len(data)<1 and len(q_list_Student) <1:
            #     token_where_string= " tk.id < 1 "
            ErrorLevelSelected= form.cleaned_data['ErrorLevelSelected']
            if ErrorLevelSelected and ErrorLevelSelected!='Nothing selected' and ErrorLevelSelected!='-1'  :
                ErrorLevelSelected=ErrorLevelSelected.replace("phonographic mapping","PG")
                ErrorLevelSelected=ErrorLevelSelected.replace("syllabic principles","SL")
                ErrorLevelSelected=ErrorLevelSelected.replace("morpheme constancy","MO")
                ErrorLevelSelected=ErrorLevelSelected.replace("morphosyntactic principles","SN")
                strlist=multiselectAsList(ErrorLevelSelected)
                subqstr="0=1" 
                for strval in  strlist:
                    subqstr=subqstr + " or error_level like '%%{}%%' ".format(strval.strip()) 
                token_where_string=token_where_string + " {} ({}) ".format(stropr,subqstr) 
                stropr="and"
                # my_string = "','".join(strlist) 
                # token_where_string=token_where_string + "and error_level in ('{}') ".format(my_string) 
             
            StudentIDSelected= form.cleaned_data['StudentIDSelected']
            if StudentIDSelected and StudentIDSelected!='Nothing selected' and StudentIDSelected!='-1' :
                strlist=multiselectAsList(StudentIDSelected)
                my_string = "','".join(str(v).strip() for v in strlist) 
                token_where_string=token_where_string + "{} st.number in ('{}') ".format(stropr,my_string)
                stropr="and"


            StudentStorySelected= form.cleaned_data['StudentStorySelected']
            if StudentStorySelected and StudentStorySelected!='Nothing selected' and StudentStorySelected!='-1' : 
                strlist=multiselectAsList(StudentStorySelected)
                my_string = "','".join(str(v).strip() for v in strlist) 
                token_where_string=token_where_string + " {} story in ('{}')".format(stropr,my_string)
                stropr="and"


            ErrorKOFSelected= form.cleaned_data['ErrorKOFSelected']
           
            if ErrorKOFSelected and ErrorKOFSelected!='Nothing selected' and ErrorKOFSelected!='-1': 
                ErrorKOFSelected=ErrorKOFSelected.replace("grapheme combinations","err_graph_comb")
                ErrorKOFSelected=ErrorKOFSelected.replace("marked graphemes","err_graph_marked")
                ErrorKOFSelected=ErrorKOFSelected.replace("ie","err_ie")
                ErrorKOFSelected=ErrorKOFSelected.replace("silent schwa","err_schwa_silent")
                ErrorKOFSelected=ErrorKOFSelected.replace("double vowels","err_doubleV")
                ErrorKOFSelected=ErrorKOFSelected.replace("other double consonants","err_doubleC_other")
                ErrorKOFSelected=ErrorKOFSelected.replace("double consonant spellings","err_doubleC_syl")
                ErrorKOFSelected=ErrorKOFSelected.replace("vowel-lengthening","err_h_length")
                ErrorKOFSelected=ErrorKOFSelected.replace("syllable-separating","err_h_sep")
                ErrorKOFSelected=ErrorKOFSelected.replace("vocalic","err_r_voc")
                ErrorKOFSelected=ErrorKOFSelected.replace("final devoicing","err_devoice_final")
                ErrorKOFSelected=ErrorKOFSelected.replace("g-spirantization","err_g_spirant")
                ErrorKOFSelected=ErrorKOFSelected.replace("morpheme boundary","err_morph_bound")
                strlist=multiselectAsList(ErrorKOFSelected)
                subqstr="0=1" 
                for strval in  strlist:
                    subqstr=subqstr + " or {}=1  ".format(strval.strip())
                token_where_string=token_where_string + " {} ({})".format(stropr,subqstr)
                stropr="and"

                     
                    

                
            
            KOFSelected= form.cleaned_data['KOFSelected']
            if KOFSelected and KOFSelected!='Nothing selected' and KOFSelected!='-1':
                KOFSelected=KOFSelected.replace("grapheme combinations","graph_comb")
                KOFSelected=KOFSelected.replace("marked graphemes","graph_marked")
                KOFSelected=KOFSelected.replace("ie","ie")
                KOFSelected=KOFSelected.replace("silent schwa","schwa_silent")
                KOFSelected=KOFSelected.replace("double vowels","doubleV")
                KOFSelected=KOFSelected.replace("other double consonants","doubleC_other")
                KOFSelected=KOFSelected.replace("double consonant spellings","doubleC_syl")
                KOFSelected=KOFSelected.replace("vowel-lengthening","h_length")
                KOFSelected=KOFSelected.replace("syllable-separating","h_sep")
                KOFSelected=KOFSelected.replace("vocalic","err_r_voc")
                KOFSelected=KOFSelected.replace("final devoicing","devoice_final")
                KOFSelected=KOFSelected.replace("g-spirantization","g_spirant")
                KOFSelected=KOFSelected.replace("morpheme boundary","morph_bound")
                strlist=multiselectAsList(KOFSelected)
                subqstr="0=1"
                for strval in  strlist:
                    subqstr=subqstr + " or {}=1  ".format(strval.strip())
                token_where_string=token_where_string + " {} ({})  ".format(stropr,subqstr)
                stropr="and"


            # KOF= form.cleaned_data['KOF'] 
            # ErrorKOF= form.cleaned_data['ErrorKOF']       
            strcommand="""SELECT * FROM tbltokenbase as tk left JOIN students as st on st.t1=tk.text_id or st.T2=tk.text_id or st.T3=tk.text_id or st.T4=tk.text_id or st.T5=tk.text_id or st.T6=tk.text_id or st.T7=tk.text_id or st.T8=tk.text_id or st.T9=tk.text_id or st.T10=tk.text_id  
            where 
             {}
             {} 
             """.format(token_where_string,student_where_string).replace("\n","") 
            Token_Student=list(models.Tbltokenbase.objects.raw(strcommand))
            if Token_Student and len(Token_Student)>0 :      
            #Average Token Pro story 

                strcommandML="""  select tt.Id, count(orig) as origcount ,story from 
                (SELECT tk.Id as Id,st.multilingual as multilingual  ,orig, target, story FROM tbltokenbase as tk
                left JOIN students as st on st.t1=tk.text_id or st.T2=tk.text_id or st.T3=tk.text_id or st.T4=tk.text_id or st.T5=tk.text_id or st.T6=tk.text_id or st.T7=tk.text_id or st.T8=tk.text_id or st.T9=tk.text_id or st.T10=tk.text_id  
                where {}{} and multilingual='ja' GROUP by story,orig) as tt GROUP by story
                """.format(token_where_string,student_where_string).replace("\n","")
                strcommandGerman="""select tt.Id, count(orig) as origcount,story from 
                (SELECT tk.Id as Id,st.multilingual as multilingual  ,orig, target, story FROM tbltokenbase as tk
                left JOIN students as st on st.t1=tk.text_id or st.T2=tk.text_id or st.T3=tk.text_id or st.T4=tk.text_id or st.T5=tk.text_id or st.T6=tk.text_id or st.T7=tk.text_id or st.T8=tk.text_id or st.T9=tk.text_id or st.T10=tk.text_id  
                where {}{} and multilingual='nein' GROUP by story,orig) as tt GROUP by story
                """.format(token_where_string,student_where_string).replace("\n","")
                strcommandKA=""" select tt.Id, count(orig) as origcount,story from 
                (SELECT tk.Id as Id,st.multilingual as multilingual ,orig, target, story FROM tbltokenbase as tk
                left JOIN students as st on st.t1=tk.text_id or st.T2=tk.text_id or st.T3=tk.text_id or st.T4=tk.text_id or st.T5=tk.text_id or st.T6=tk.text_id or st.T7=tk.text_id or st.T8=tk.text_id or st.T9=tk.text_id or st.T10=tk.text_id 
                where {}{} and multilingual='k.A.' GROUP by story,orig) as tt GROUP by story 
                """.format(token_where_string,student_where_string).replace("\n","")
                
                AverageStoryMultilanguage=list(models.Tbltokenbase.objects.raw(strcommandML))
                AverageStoryGerman=list(models.Tbltokenbase.objects.raw(strcommandGerman))
                AverageStoryNA=list(models.Tbltokenbase.objects.raw(strcommandKA))

                #Average Type Per Story
        
                
                strcommandtypeML="""  select tt.Id, count(target) as targetcount ,story from 
                (SELECT tk.Id as Id,st.multilingual as multilingual , target, story FROM tbltokenbase as tk
                left JOIN students as st on st.t1=tk.text_id or st.T2=tk.text_id or st.T3=tk.text_id or st.T4=tk.text_id or st.T5=tk.text_id or st.T6=tk.text_id or st.T7=tk.text_id or st.T8=tk.text_id or st.T9=tk.text_id or st.T10=tk.text_id 
                where {}{} and multilingual='ja' GROUP by story,target) as tt GROUP by story
                """.format(token_where_string,student_where_string).replace("\n","")
                strcommandtypeGerman="""select tt.Id, count(target) as targetcount,story from 
                (SELECT tk.Id as Id,st.multilingual as multilingual , target, story FROM tbltokenbase as tk
                left JOIN students as st on st.t1=tk.text_id or st.T2=tk.text_id or st.T3=tk.text_id or st.T4=tk.text_id or st.T5=tk.text_id or st.T6=tk.text_id or st.T7=tk.text_id or st.T8=tk.text_id or st.T9=tk.text_id or st.T10=tk.text_id 
                where {}{} and multilingual='nein' GROUP by story,target) as tt GROUP by story
                """.format(token_where_string,student_where_string).replace("\n","")
                strcommandtypeKA=""" select tt.Id, count(target) as targetcount,story from 
                (SELECT tk.Id as Id,st.multilingual as multilingual , target, story FROM tbltokenbase as tk
                left JOIN students as st on st.t1=tk.text_id or st.T2=tk.text_id or st.T3=tk.text_id or st.T4=tk.text_id or st.T5=tk.text_id or st.T6=tk.text_id or st.T7=tk.text_id or st.T8=tk.text_id or st.T9=tk.text_id or st.T10=tk.text_id 
                where {}{} and multilingual='k.A.' GROUP by story,target) as tt GROUP by story 
                """.format(token_where_string,student_where_string).replace("\n","")
                
                AverageStoryTypeMultilanguage=list(models.Tbltokenbase.objects.raw(strcommandtypeML))
                AverageStoryTypeGerman=list(models.Tbltokenbase.objects.raw(strcommandtypeGerman))
                AverageStoryTypeNA=list(models.Tbltokenbase.objects.raw(strcommandtypeKA))

                # Error Level
                strcommandErrorML=""" select tt.Id, count(error_level) as errcount ,story from 
                (SELECT tk.Id as Id,st.multilingual as multilingual , error_level, target, story FROM tbltokenbase as tk 
                left JOIN students as st on st.t1=tk.text_id or st.T2=tk.text_id or st.T3=tk.text_id or 
                st.T4=tk.text_id or st.T5=tk.text_id or st.T6=tk.text_id or st.T7=tk.text_id or st.T8=tk.text_id or st.T9=tk.text_id or st.T10=tk.text_id 
                where {}{} and multilingual='ja'  and  error_level<>'' GROUP by story,tk.error_level) as tt GROUP by story order by story
                """.format(token_where_string,student_where_string).replace("\n","")
                AverageStoryERRML=list(models.Tbltokenbase.objects.raw(strcommandErrorML))

                strcommandErrorGer="""  select tt.Id, count(error_level) as errcount ,story from 
                (SELECT tk.Id as Id,st.multilingual as multilingual , error_level, target, story FROM tbltokenbase as tk 
                left JOIN students as st on st.t1=tk.text_id or st.T2=tk.text_id or st.T3=tk.text_id or 
                st.T4=tk.text_id or st.T5=tk.text_id or st.T6=tk.text_id or st.T7=tk.text_id or st.T8=tk.text_id or st.T9=tk.text_id or st.T10=tk.text_id 
                where {}{} and multilingual='nein'  and  error_level<>'' GROUP by story,tk.error_level) as tt GROUP by story order by story
                """.format(token_where_string,student_where_string).replace("\n","")

                AverageStoryERRGerman=list(models.Tbltokenbase.objects.raw(strcommandErrorGer))

                strcommandErrorKA=""" select tt.Id, count(error_level) as errcount ,story from 
                (SELECT tk.Id as Id,st.multilingual as multilingual ,error_level, target, story FROM tbltokenbase as tk 
                left JOIN students as st on st.t1=tk.text_id or st.T2=tk.text_id or st.T3=tk.text_id or 
                st.T4=tk.text_id or st.T5=tk.text_id or st.T6=tk.text_id or st.T7=tk.text_id or st.T8=tk.text_id or st.T9=tk.text_id or st.T10=tk.text_id  
                where {}{} and multilingual='k.a.' and  error_level<>'' GROUP by story,tk.error_level) as tt GROUP by story order by story
                """.format(token_where_string,student_where_string).replace("\n","")
                AverageStoryERRKA=list(models.Tbltokenbase.objects.raw(strcommandErrorKA))
                
                # POS
                strcommandPosKA=""" select tt.Id, count(pos) as poscount ,story from 
                (SELECT tk.Id as Id,st.multilingual as multilingual ,pos,error_level, target, story FROM tbltokenbase as tk 
                left JOIN students as st on st.t1=tk.text_id or st.T2=tk.text_id or st.T3=tk.text_id or 
                st.T4=tk.text_id or st.T5=tk.text_id or st.T6=tk.text_id or st.T7=tk.text_id or st.T8=tk.text_id or st.T9=tk.text_id or st.T10=tk.text_id  
                where {}{} and multilingual='ja' and  pos<>'' GROUP by story,tk.pos) as tt GROUP by story order by story
                """.format(token_where_string,student_where_string).replace("\n","")
                AverageStoryPosML=list(models.Tbltokenbase.objects.raw(strcommandPosKA))

                strcommandPosKA=""" select tt.Id, count(pos) as poscount ,story from 
                (SELECT tk.Id as Id,st.multilingual as multilingual ,pos,error_level, target, story FROM tbltokenbase as tk 
                left JOIN students as st on st.t1=tk.text_id or st.T2=tk.text_id or st.T3=tk.text_id or 
                st.T4=tk.text_id or st.T5=tk.text_id or st.T6=tk.text_id or st.T7=tk.text_id or st.T8=tk.text_id or st.T9=tk.text_id or st.T10=tk.text_id  
                where {}{} and multilingual='nein' and  pos<>'' GROUP by story,tk.pos) as tt GROUP by story order by story
                """.format(token_where_string,student_where_string).replace("\n","")

                AverageStoryPosGerman=list(models.Tbltokenbase.objects.raw(strcommandPosKA))

                strcommandPosKA=""" select tt.Id, count(pos) as poscount ,story from 
                (SELECT tk.Id as Id,st.multilingual as multilingual ,pos,error_level, target, story FROM tbltokenbase as tk 
                left JOIN students as st on st.t1=tk.text_id or st.T2=tk.text_id or st.T3=tk.text_id or 
                st.T4=tk.text_id or st.T5=tk.text_id or st.T6=tk.text_id or st.T7=tk.text_id or st.T8=tk.text_id or st.T9=tk.text_id or st.T10=tk.text_id  
                where {}{} and multilingual='k.a.' and  pos<>'' GROUP by story,tk.pos) as tt GROUP by story order by story
                """.format(token_where_string,student_where_string).replace("\n","")
                AverageStoryPosKA=list(models.Tbltokenbase.objects.raw(strcommandPosKA))
                
            
                listOfStory=["Eis","Weg_2","Frosch","Jenga","Staubsauger","Weg_3","Schule","Fundbuero","Seilbahn","Weg_4"]
                listOfStoryValue=[0,0,0,0,0,0,0,0,0,0]
                #Token add data to model
                arrtoken=[]  
                names=[]
                for p in AverageStoryMultilanguage:
                    names.append(str(p.story))
                    indexval=listOfStory.index(str(p.story))
                    listOfStoryValue[indexval]=p.origcount
                    arrtoken.append(p.origcount)    

                
                    

                ChartStoryDeveloped.storytokenvaluesML=listOfStoryValue
                ChartStoryDeveloped.StoryNameToken=listOfStory
                listOfStoryValue=[0,0,0,0,0,0,0,0,0,0]
                arrtoken=[] 
                arrtype=[]
                for p in AverageStoryGerman:
                    arrtoken.append(p.origcount)    
                    indexval=listOfStory.index(str(p.story))
                    listOfStoryValue[indexval]=p.origcount

                ChartStoryDeveloped.storytokenvaluesGER=listOfStoryValue
                listOfStoryValue=[0,0,0,0,0,0,0,0,0,0]
                arrtoken=[] 
                arrtype=[]
                for p in AverageStoryNA:
                    arrtoken.append(p.origcount)  
                    indexval=listOfStory.index(str(p.story))
                    listOfStoryValue[indexval]=p.origcount  
                
                ChartStoryDeveloped.storytokenvaluesKA=listOfStoryValue
                #Target add data to model 

                arrtype=[]
                names=[]
                listOfStoryValue=[0,0,0,0,0,0,0,0,0,0]
                for p in AverageStoryTypeMultilanguage:
                    arrtype.append(p.targetcount)   
                    indexval=listOfStory.index(str(p.story))
                    listOfStoryValue[indexval]=p.targetcount
                    names.append(str(p.story))

                ChartStoryDeveloped.storytypevaluesML=listOfStoryValue
                ChartStoryDeveloped.StoryNameType=listOfStory
                
                arrtype=[]
                listOfStoryValue=[0,0,0,0,0,0,0,0,0,0]
                for p in AverageStoryTypeGerman:
                    indexval=listOfStory.index(str(p.story))
                    listOfStoryValue[indexval]=p.targetcount
                    arrtype.append(p.targetcount) 

                ChartStoryDeveloped.storytypevaluesGER=listOfStoryValue

                arrtype=[]
                listOfStoryValue=[0,0,0,0,0,0,0,0,0,0]
                for p in AverageStoryTypeNA:
                    indexval=listOfStory.index(str(p.story))
                    listOfStoryValue[indexval]=p.targetcount
                    arrtype.append(p.targetcount)   
                
                ChartStoryDeveloped.storytypevaluesKA =listOfStoryValue


                #Error Level add data to model
                listOfStoryValue=[0,0,0,0,0,0,0,0,0,0]
                arrErr=[] 
                names=[]
                for p in AverageStoryERRML:
                    arrErr.append(p.errcount)   
                    indexval=listOfStory.index(str(p.story))
                    listOfStoryValue[indexval]=p.errcount

                ChartStoryDeveloped.storyErrorvaluesML=listOfStoryValue
                ChartStoryDeveloped.StoryNameError=listOfStory
                arrErr=[] 
                listOfStoryValue=[0,0,0,0,0,0,0,0,0,0]

                for p in AverageStoryERRGerman:
                    arrErr.append(p.errcount) 
                    indexval=listOfStory.index(str(p.story))
                    listOfStoryValue[indexval]=p.errcount  
                ChartStoryDeveloped.storyErrorvaluesGER=listOfStoryValue
                arrErr=[] 
                listOfStoryValue=[0,0,0,0,0,0,0,0,0,0]
                
                for p in AverageStoryERRKA:
                    arrErr.append(p.errcount)   
                    indexval=listOfStory.index(str(p.story))
                    listOfStoryValue[indexval]=p.errcount
                ChartStoryDeveloped.storyErrorvaluesKA=listOfStoryValue
                #POS add data to model
                    
                arrpos=[] 
                names=[]
                
                listOfStoryValue=[0,0,0,0,0,0,0,0,0,0]
                for p in AverageStoryPosML:
                    names.append(str(p.story))    
                    indexval=listOfStory.index(str(p.story))
                    listOfStoryValue[indexval]=p.poscount

                ChartStoryDeveloped.storyPosvaluesML=listOfStoryValue   
                ChartStoryDeveloped.StoryNamePos= listOfStory

                arrpos=[] 
                listOfStoryValue=[0,0,0,0,0,0,0,0,0,0]
                for p in AverageStoryPosGerman:
                    indexval=listOfStory.index(str(p.story))
                    listOfStoryValue[indexval]=p.poscount
                ChartStoryDeveloped.storyPosvaluesGER=listOfStoryValue   
                
                arrpos=[] 
                listOfStoryValue=[0,0,0,0,0,0,0,0,0,0]
                for p in AverageStoryPosKA:
                    indexval=listOfStory.index(str(p.story))
                    listOfStoryValue[indexval]=p.poscount
                ChartStoryDeveloped.storyPosvaluesKA=listOfStoryValue   
                
                
                #donat chart

                getstrstorycat=""" SELECT tk.Id, story,count(orig) as tokencount  FROM tbltokenbase as tk INNER JOIN
                students as st on st.t1=tk.text_id or st.T2=tk.text_id or st.T3=tk.text_id or st.T4=tk.text_id or st.T5=tk.text_id or 
                st.T6=tk.text_id or st.T7=tk.text_id or st.T8=tk.text_id  or st.T9=tk.text_id or st.T10=tk.text_id  
                where 
                {}
                {} group by story 
                """.format(token_where_string,student_where_string).replace("\n","")
                getcountbyStory=list(models.Tbltokenbase.objects.raw(getstrstorycat))
                labels=[] 
                values=[] 
                for p in getcountbyStory:
                    labels.append(str(p.story))   
                    values.append(p.tokencount)
                DonchartModel.agecat=labels
                DonchartModel.storytokenvalues=values
                
                getstrstorytype=""" 
                select tt.Id, count(target) as targetcount ,story from (SELECT tk.Id as Id, target, story FROM tbltokenbase as tk left JOIN students as st on st.t1=tk.text_id or st.T2=tk.text_id or st.T3=tk.text_id or st.T4=tk.text_id or st.T5=tk.text_id or st.T6=tk.text_id or st.T7=tk.text_id or st.T8=tk.text_id  or st.T9=tk.text_id or st.T10=tk.text_id  
                where 
                {}
                {} 
                GROUP by story,target) as tt GROUP by story
                """.format(token_where_string,student_where_string).replace("\n","")
                getcountbyStoryType=list(models.Tbltokenbase.objects.raw(getstrstorytype))

                labels=[] 
                values=[] 
                for p in getcountbyStoryType:
                    labels.append(str(p.story))   
                    values.append(p.targetcount)                              
                DonchartModel.storytypecat=  labels
                DonchartModel.storytypevalues=  values


                StrWordNumber=""" SELECT  tk.Id,   st.multilingual as multilingual, count(multilingual) as spcount FROM tbltokenbase as tk left JOIN students as st on st.t1=tk.text_id or st.T2=tk.text_id or st.T3=tk.text_id or st.T4=tk.text_id or st.T5=tk.text_id or st.T6=tk.text_id or st.T7=tk.text_id or st.T8=tk.text_id  or st.T9=tk.text_id or st.T10=tk.text_id  
                where 
                {}
                {} group by st.multilingual ORDER by st.multilingual
                """.format(token_where_string,student_where_string).replace("\n","")
                ChartWord=list(models.Tbltokenbase.objects.raw(StrWordNumber))

                labels=[] 
                values=[] 
                for p in ChartWord:
                    labels.append(str(p.multilingual))   
                    values.append(p.spcount)
                
                ChartBarNumberWord.Wordcat=labels    
                ChartBarNumberWord.WordCount=values

                StrAggregatedLemma=""" SELECT  tk.Id,   chl_lemma,
                cast(avg(chl_lemma_norm) as decimal(10,2)) as freqper1M,
                cast(avg(chl_lemma_abs) as decimal(10,2)) as freqabsolute,
                cast(avg(chl_type_norm) as decimal(10,2)) as Wordformfreqabsolute
                
                FROM tbltokenbase as tk left JOIN students as st on st.t1=tk.text_id or st.T2=tk.text_id or st.T3=tk.text_id or st.T4=tk.text_id or st.T5=tk.text_id or st.T6=tk.text_id or st.T7=tk.text_id or st.T8=tk.text_id  or st.T9=tk.text_id or st.T10=tk.text_id  
                where 
                {}
                {} group by chl_lemma  ORDER by chl_lemma
                """.format(token_where_string,student_where_string).replace("\n","")

                
                AggregatedLema=list(models.Tbltokenbase.objects.raw(StrAggregatedLemma))

                StrAggregatedText=""" SELECT  tk.Id,   text_id ,
                cast(avg(chl_lemma_norm) as decimal(10,2)) as freqper1M,
                cast(avg(chl_lemma_abs) as decimal(10,2)) as freqabsolute,
                cast(avg(chl_type_norm) as decimal(10,2)) as Wordformfreqabsolute
                
                FROM tbltokenbase as tk left JOIN students as st on st.t1=tk.text_id or st.T2=tk.text_id or st.T3=tk.text_id or st.T4=tk.text_id or st.T5=tk.text_id or st.T6=tk.text_id or st.T7=tk.text_id or st.T8=tk.text_id  or st.T9=tk.text_id or st.T10=tk.text_id  
                where 
                {}
                {} group by text_id   ORDER by text_id 
                """.format(token_where_string,student_where_string).replace("\n","")
                AggregatedText=list(models.Tbltokenbase.objects.raw(StrAggregatedText))
            
                StrAggregatedGlobal=""" SELECT  tk.Id,   text_id ,
                cast(avg(chl_lemma_norm) as decimal(10,2)) as freqper1M,
                cast(avg(chl_lemma_abs) as decimal(10,2)) as freqabsolute,
                cast(avg(chl_type_norm) as decimal(10,2)) as Wordformfreqabsolute
                
                FROM tbltokenbase as tk left JOIN students as st on st.t1=tk.text_id or st.T2=tk.text_id or st.T3=tk.text_id or st.T4=tk.text_id or st.T5=tk.text_id or st.T6=tk.text_id or st.T7=tk.text_id or st.T8=tk.text_id  or st.T9=tk.text_id or st.T10=tk.text_id  
                where 
                {}
                {} 
                """.format(token_where_string,student_where_string).replace("\n","")
                AggregatedGlobal=list(models.Tbltokenbase.objects.raw(StrAggregatedGlobal))
                
                strcommandChartAge="""
                select tt.Id  ,
                SUM(IF(lt_9 > 0,1,0)) as cntlt_9 ,
                SUM(IF(btw_9_10 > 0,1,0)) as cntbtw_9_10,
                SUM(IF(btw_10_11 > 0,1,0)) as cntbtw_10_11,
                SUM(IF(btw_11_12 > 0,1,0)) as cntbtw_11_12,
                SUM(IF(gt_12 > 0,1,0)) as cntgt_12
                from (SELECT tk.Id as Id,   SUM(IF((alt1) < 9,1,0)) as lt_9,
                                SUM(IF( (alt1) BETWEEN 9 and 10,1,0) ) as btw_9_10,
                                SUM(IF((alt1) BETWEEN 10.01 and 11,1,0)) as btw_10_11,
                                SUM(IF((alt1) BETWEEN 11.01 and 12,1,0)) as btw_11_12,
                                SUM(IF((alt1) >12,1,0)) as gt_12 ,target 
                                FROM tbltokenbase as tk left JOIN students as st on st.t1=tk.text_id or st.T2=tk.text_id or st.T3=tk.text_id or st.T4=tk.text_id or st.T5=tk.text_id or st.T6=tk.text_id or st.T7=tk.text_id or st.T8=tk.text_id  or st.T9=tk.text_id or st.T10=tk.text_id  
                                        where 
                                            {}
                                            {} 
                                            GROUP by orig) as tt
                """.format(token_where_string,student_where_string).replace("\n","")
                # strcommandChartAge=""" SELECT tk.Id,    SUM(IF((alt1) < 9,1,0)) as lt_9,
                #                 SUM(IF( (alt1) BETWEEN 9 and 10,1,0) ) as btw_9_10,
                #                 SUM(IF((alt1) BETWEEN 10.01 and 11,1,0)) as btw_10_11,
                #                 SUM(IF((alt1) BETWEEN 11.01 and 12,1,0)) as btw_11_12,
                #                 SUM(IF((alt1) >12,1,0)) as 'gt_12'  FROM tbltokenbase as tk left JOIN students as st on st.t1=tk.text_id or st.T2=tk.text_id or st.T3=tk.text_id or st.T4=tk.text_id or st.T5=tk.text_id or st.T6=tk.text_id or st.T7=tk.text_id or st.T8=tk.text_id  or st.T9=tk.text_id or st.T10=tk.text_id  
                #                         where 
                #                             {}
                #                             {} 
                #  """.format(token_where_string,student_where_string).replace("\n","")
                ChartAge=list(models.Tbltokenbase.objects.raw(strcommandChartAge))
                values=[] 
                for p in ChartAge:
                    values.append( int(p.cntlt_9))   
                    values.append( int(p.cntbtw_9_10))   
                    values.append( int(p.cntbtw_10_11))   
                    values.append( int(p.cntbtw_11_12))   
                    values.append( int(p.cntgt_12))   
                

                DonchartModel.agetokenvalues=values 

                #Age Type  
                
                strcommandChartAgeType="""
                select Id  ,SUM(IF(lt_9 > 0,1,0)) as cntlt_9 ,
                SUM(IF(btw_9_10 > 0,1,0)) as cntbtw_9_10,
                SUM(IF(btw_10_11 > 0,1,0)) as cntbtw_10_11,
                SUM(IF(btw_11_12 > 0,1,0)) as cntbtw_11_12,
                SUM(IF(gt_12 >0,1,0)) as cntgt_12
                from (SELECT tk.Id as Id,SUM(IF((alt1) < 9,1,0)) as lt_9,
                                SUM(IF( (alt1) BETWEEN 9 and 10,1,0) ) as btw_9_10,
                                SUM(IF((alt1) BETWEEN 10.01 and 11,1,0)) as btw_10_11,
                                SUM(IF((alt1) BETWEEN 11.01 and 12,1,0)) as btw_11_12,
                                SUM(IF((alt1) >12,1,0)) as gt_12 ,target 
                                FROM tbltokenbase as tk left JOIN students as st on st.t1=tk.text_id or st.T2=tk.text_id or st.T3=tk.text_id or st.T4=tk.text_id or st.T5=tk.text_id or st.T6=tk.text_id or st.T7=tk.text_id or st.T8=tk.text_id  or st.T9=tk.text_id or st.T10=tk.text_id  
                                        where 
                                            {}
                                            {} 
                                            GROUP by target) as tt
                """.format(token_where_string,student_where_string).replace("\n","")
    
                ChartAgeType=list(models.Tbltokenbase.objects.raw(strcommandChartAgeType))
                values=[] 
                for p in ChartAgeType:
                    values.append( int(p.cntlt_9))   
                    values.append( int(p.cntbtw_9_10))   
                    values.append( int(p.cntbtw_10_11))   
                    values.append( int(p.cntbtw_11_12))   
                    values.append( int(p.cntgt_12))   
                DonchartModel.agetypevalues=values

    else:
        form=SearchViewModel.SearchItem()
        showpanel='hide'

     

            
       
    minmaxmodel=SearchViewModel.MinMaxSearchValue()
    minmaxmodel=MaxMinSliderLoad(minmaxmodel)

 
    
    datacount=SearchViewModel.DataCount()
    datacount.observations  = tbltoken.count()
    datacount.students  = models.Students.objects.count()
    datacount.wordforms  = tbltype.count()
    datacount.texts  = tbltoken.values('text_id').distinct().count()
    datacount.lemmas  = tbltoken.exclude(chl_lemma__isnull=True).values('chl_lemma').distinct().count()
    stdids=models.Students.objects.only('number') 
 
    
    

    context={'form': form,
    'result':resultmodel,
    'maxminModel':minmaxmodel,
    'fields' :ShowCols,
    'fieldsLabel' :ShowfieldsLabel,
    'showpanel':showpanel,
    # Token_Student._meta.get_fields(),
    'datacount':datacount,
    'stdids':stdids,
    'DonchartModel':DonchartModel,
    'Token_Student':Token_Student,
    'str':my_string,
    'strcommand':strcommand,
    'ChartBarNumberWord':ChartBarNumberWord,
    'ChartStoryDeveloped':ChartStoryDeveloped,
    'AggregatedGlobal':AggregatedGlobal,
    'AggregatedText':AggregatedText,
    'AggregatedLema':AggregatedLema,
    'StudentIDSelected':StudentIDSelected,
    'ListFilterItems':', '.join(str(v) for v in  ListFilterItems  )
    }
    return render(request, "MainSearch.html", context)

    