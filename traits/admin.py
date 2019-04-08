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
    resource_class = PublocalResource

class TraitAdmin(ImportExportModelAdmin):
    list_display = ('__str__', 'pubref')
    resource_class = TraitResource

admin.site.register(Trait, TraitAdmin)
admin.site.register(Publocal, PublocalAdmin)
