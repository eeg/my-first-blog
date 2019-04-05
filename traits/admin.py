from django.contrib import admin
from .models import Trait, Publocal

from import_export.admin import ImportExportModelAdmin
from .resources import TraitResource, PublocalResource

class TraitInline(admin.TabularInline):
    model = Trait
    show_change_link = True

class PublocalAdmin(ImportExportModelAdmin):
    inlines = [
        TraitInline,
    ]

class TraitAdmin(ImportExportModelAdmin):
    list_display = ('__str__', 'pubref')

admin.site.register(Trait, TraitAdmin)
admin.site.register(Publocal, PublocalAdmin)
