from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Trait
from .resources import TraitResource

class TraitInline(admin.TabularInline):
    model = Trait
    show_change_link = True

class TraitAdmin(ImportExportModelAdmin):
    list_display = ('__str__', 'pubref')
    resource_class = TraitResource

admin.site.register(Trait, TraitAdmin)
