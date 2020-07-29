
from django import forms


class SearchItem(forms.Form):
    # TargetSelects=('choos','Start with','Endwith','end with')
    # OrigSelects=(required=False,'choos','Start with','Endwith','end with')
    Lemma= forms.CharField(required=False, label="Lemma",max_length=200)
    Target= forms.CharField(required=False, label="Target",max_length=200)
    Orig=forms.CharField(required=False,label="Orig",max_length=200)

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
    
