from pickle import FALSE

from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.

class Saglik(models.Model):


    kodu = models.CharField(max_length = 10)
    sbkodu = models.CharField(max_length = 7)
    kurumadı = models.CharField(max_length = 70)
    pozisyon = models.CharField(max_length = 17)
    sehir = models.CharField(max_length = 17)
    sayi = models.CharField(max_length = 17) 

    class Meta:
        abstract = True
        
    def __str__(self):
        return 'Tip: {0} Kurum Adı: {1}'.format(self.kodu, self.kurumadı)

class Ebe(Saglik):
    pass

class Hemsire(Saglik):
    pass

class Yil2021(Saglik):
    pass

