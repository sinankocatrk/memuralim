from django import forms
from .models import *

class EbeForm(forms.ModelForm):
    class Meta:
        model = Ebe
        fields = ('kodu', 'sbkodu', 'kurumadı','sehir','sayi')


class Yil2021eForm(forms.ModelForm):
    class Meta:
        model = Yil2021
        fields = ('kodu', 'sbkodu', 'kurumadı','pozizyon','sehir','sayi')

