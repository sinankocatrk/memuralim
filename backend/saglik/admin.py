from django.contrib import admin

from saglik.models import Ebe,Hemsire,Saglik
from import_export.admin import ImportExportModelAdmin

@admin.register(Ebe,Hemsire)

class VievAdmin(ImportExportModelAdmin):
    
    pass

