from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from simple_history.admin import SimpleHistoryAdmin
from .models import Trait
from .resources import TraitResource

class TraitInline(admin.TabularInline):
    model = Trait
    show_change_link = True

class TraitAdmin(ImportExportModelAdmin, SimpleHistoryAdmin):
    list_display = ('__str__', 'pubref')
    #  history_list_display = ['breeding_system', 'isi', 'pubref']
    history_list_display = [field.name for field in Trait._meta.get_fields()]
    resource_class = TraitResource

admin.site.register(Trait, TraitAdmin)
