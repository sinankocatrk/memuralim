from django.contrib import admin

from saglik.models import Ebe,Hemsire,Saglik, Yil2021
from import_export.admin import ImportExportModelAdmin

@admin.register(Ebe,Hemsire,Yil2021)

class VievAdmin(ImportExportModelAdmin):
    
    pass

