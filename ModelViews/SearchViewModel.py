
from django import forms


class SearchItem(forms.Form):
    # TargetSelects=('choos','Start with','Endwith','end with')
    # OrigSelects=(required=False,'choos','Start with','Endwith','end with')
    Lemma= forms.CharField(required=False, label="Lemma",max_length=200 )
    Target= forms.CharField(required=False, label="Target" ,max_length=200)
    Orig=forms.CharField(required=False,label="Orig",max_length=200 )
    LemmaSelect= forms.IntegerField(required=False, label="LemmaSelect")
    max_lemma_freq= forms.FloatField(required=False, label="max_lemma_freq" )
    min_lemma_freq= forms.FloatField(required=False, label="min_lemma_freq" )
    max_lemma_absolute= forms.FloatField(required=False, label="max_lemma_absolute" )
    min_lemma_absolute= forms.FloatField(required=False, label="min_lemma_absolute" )
    max_lemma_Zipf= forms.FloatField(required=False, label="max_lemma_Zipf" )
    min_lemma_Zipf= forms.FloatField(required=False, label="min_lemma_Zipf" )
    TargetSelect= forms.IntegerField(required=False, label="TargetSelect")
    OrigSelect= forms.IntegerField(required=False, label="OrigSelect")
    max_word_phonemes= forms.FloatField(required=False, label="max_word_phonemes" )
    min_word_phonemes= forms.FloatField(required=False, label="min_word_phonemes" )
    max_word_graphemes= forms.FloatField(required=False, label="max_word_graphemes" )
    min_word_graphemes= forms.FloatField(required=False, label="min_word_graphemes" )
    max_word_syllables= forms.FloatField(required=False, label="max_word_syllables" )
    min_word_syllables= forms.FloatField(required=False, label="min_word_syllables" )
    max_word_morphemes= forms.FloatField(required=False, label="max_word_morphemes" )
    min_word_morphemes= forms.FloatField(required=False, label="min_word_morphemes" )
    
    IsFunktion= forms.BooleanField(required=False, label="max_word_phonemes")
    IsLexion= forms.BooleanField(required=False, label="max_word_phonemes")
    POSSelect= forms.IntegerField(required=False, label="max_word_phonemes")
    POS= forms.CharField(required=False, label="max_word_phonemes" ,max_length=200)
    SyllableTypeSelect= forms.IntegerField(required=False, label="max_word_phonemes")
    SyllableType= forms.CharField(required=False, label="max_word_phonemes" ,max_length=200)
    max_word_absolute= forms.FloatField(required=False, label="max_word_phonemes" )
    min_word_absolute= forms.FloatField(required=False, label="max_word_phonemes" )
    max_word_freq= forms.FloatField(required=False, label="max_word_phonemes" )
    min_word_freq= forms.FloatField(required=False, label="max_word_phonemes" )
    max_word_bigram= forms.FloatField(required=False, label="max_word_phonemes" )
    min_word_bigram= forms.FloatField(required=False, label="max_word_phonemes" )
    max_word_neighbors= forms.FloatField(required=False, label="max_word_phonemes" )
    min_word_neighbors= forms.FloatField(required=False, label="max_word_phonemes" )
    max_word_OLD20= forms.FloatField(required=False, label="max_word_phonemes" )
    min_word_OLD20= forms.FloatField(required=False, label="max_word_phonemes" )
    ErrorLevel= forms.CharField(required=False, label="max_word_phonemes" ,max_length=200)
    ErrorLevelSelected= forms.IntegerField(required=False, label="max_word_phonemes")
    KOF= forms.CharField(required=False, label="max_word_phonemes" ,max_length=200)
    ErrorKOFSelected= forms.IntegerField(required=False, label="max_word_phonemes")
    ErrorKOF= forms.CharField(required=False, label="max_word_phonemes" ,max_length=200)
     
    max_Err_wordform= forms.FloatField(required=False, label="max_Err_wordform" )
    min_Err_wordform= forms.FloatField(required=False, label="min_Err_wordform" )
    
    max_Err_child= forms.FloatField(required=False, label="max_Err_child" )
    min_Err_child= forms.FloatField(required=False, label="max_Err_child" )
    
    StudentIDSelect= forms.IntegerField(required=False, label="StudentIDSelect")
    StudentID= forms.CharField(required=False, label="StudentID" ,max_length=200)
    StudentSex= forms.IntegerField(required=False, label="StudentSex")
    StudentNativecountry= forms.IntegerField(required=False, label="StudentNativecountry")
    Multilingual= forms.IntegerField(required=False, label="Multilingual")
    StudentPreferredReading= forms.IntegerField(required=False, label="StudentPreferredReading")
    StudentPreferredSpeaking= forms.IntegerField(required=False, label="StudentPreferredSpeaking")
    StudentTeachingGerman= forms.IntegerField(required=False, label="StudentTeachingGerman")
    StudentTeachingNative= forms.IntegerField(required=False, label="StudentTeachingNative")

    max_student_writing= forms.FloatField(required=False, label="max_student_writing" )
    min_student_writing= forms.FloatField(required=False, label="min_student_writing" )

    StudentOriginFather= forms.IntegerField(required=False, label="StudentOriginFather")
    StudentOriginMother= forms.IntegerField(required=False, label="StudentOriginMother")

    StudentcountryFather= forms.IntegerField(required=False, label="StudentcountryFather")
    StudentcountryMother= forms.IntegerField(required=False, label="StudentcountryMother")
    
    StudentTestTimeSelect= forms.IntegerField(required=False, label="StudentTestTimeSelect")
    StudentStorySelect= forms.IntegerField(required=False, label="StudentStorySelect")
    
    StudentStory= forms.CharField(required=False, label="StudentStory" ,max_length=200)

    StudentTestTimeSelect= forms.IntegerField(required=False, label="StudentTestTimeSelect")


    
    # Age: forms.IntegerField(50) 
    # StudentID: 
    # Nationality: str
    # ErrorLevel: str
    # Pos: str
class ShowColumnGrid:
    Showlemma:bool
    Showlemmafreqper1M=bool
    Showlemmaabsolutefreq=bool
    ShowlemmaZipfscore=bool
    Showwordform=bool
    Showwordiginal=bool
    Showwordnumberofphonemes=bool
    Showwordnumberofgraphmes=bool
    Showwordnumberofsyllables=bool
    Showwordnumberofmorphemes=bool
    Showwordpartofspeechtype=bool
    Showwordpartofspeech=bool
    Showwordsyllabletypes=bool
    Showwordabsolutefreq=bool
    Showwordfreqper1M=bool
    Showwordsummedbigramfreq=bool
    Showwordnumberofneighbors=bool
    ShowwordOLD20=bool
    ShowwordErrorlevel=bool
    ShowwordErrorKOF=bool    

class MinMaxSearchValue:
    max_no_phonemes:float
    min_no_phonemes:float
    max_norm:float
    min_norm:float
    max_abs:float
    min_abs:float
    max_no_graphemes:float
    min_no_graphemes:float
    max_no_syllables:float
    min_no_syllables:float
    max_no_morphemes:float
    min_no_morphemes:float
    max_chl_type_abs:float
    min_chl_type_abs:float
    max_chl_type_norm:float
    min_chl_type_norm:float
    max_chl_bigram_sum:float
    min_chl_bigram_sum:float
    max_chl_nei_n:float
    min_chl_nei_n:float
    max_chl_nei_OLD20:float
    min_chl_nei_OLD20:float

    max_Err_wordform:float
    min_Err_wordform:float

    max_Err_child:float
    min_Err_child:float

    max_Err_spelling:float
    min_Err_spelling:float
    max_student_writing:float
    min_student_writing:float
    
class DataCount:
    observations:float
    students:float
    wordforms	  :float
    lemmas	  :float
    texts :float
    min_abs:float    
    
class ChartDonat:
    storycat:str=[]
    storytypecat:str=[]
    storytokenvalues:str=[]
    storytypevalues:str=[]
    agecat:str=[]
    labels:str
    agetokenvalues:int=[]
    agetypevalues:float=[]
    
class ChartBarNumberWord:
    Wordcat:int=[]
    WordCount:int=[]
     



class ChartStoryDeveloped:
    def __init__(self):
        self.storytokenLabelsML = ''
        self.storytokenvaluesML = ''
        self.storytypeLabelsML = ''
        self.storytypevaluesML = ''
        self.storyErrorvaluesML = ''
        self.storyErrorLabelsML = ''
        self.storyPosvaluesML = ''
        self.storyPosLabelsML = ''

    storytokenLabelsML:str=[]
    storytokenvaluesML:str=[]
    storytypeLabelsML:str=[]
    storytypevaluesML:str=[]
    storyErrorvaluesML:str=[]
    storyErrorLabelsML:str=[]
    storyPosvaluesML:str=[]
    storyPosLabelsML:str=[]

    storytokenLabelsGER:str=[]
    storytokenvaluesGER:str=[]
    storytypeLabelsGER:str=[]
    storytypevaluesGER:str=[]
    storyErrorvaluesGER:str=[]
    storyErrorLabelsGER:str=[]
    storyPosvaluesGER:str=[]
    storyPosLabelsGER:str=[]
    
    storytokenLabelsKA:str=[]
    storytokenvaluesKA:str=[]
    storytypeLabelsKA:str=[]
    storytypevaluesKA:str=[]
    storyErrorvaluesKA:str=[]
    storyErrorLabelsKA:str=[]
    storyPosvaluesKA:str=[]
    storyPosLabelsKA:str=[]
    StoryNameToken:str=[]
    StoryNameType:str=[]
    StoryNamePos:str=[]
    StoryNameError:str=[]
    