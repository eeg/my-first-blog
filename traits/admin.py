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

    resource_class = TraitResource

    # history_list_display = ['breeding_system', 'isi', 'pubref']
    history_list_display = [field.name for field in Trait._meta.get_fields()]

    ## This prints a list of the fields that were changed in each update.
    ## Not the diff we want, but perhaps on the right track.
    #
    # history_list_display = ['get_changed_fields']
    # def get_changed_fields(self, obj):
    #     fields = []
    #     prev = obj.prev_record
    #     if prev:
    #         fields = obj.diff_against(prev).changed_fields
    #     return fields
    #
    ## misc other code/note:
    # delta = new_record.diff_against(old_record)
    # for change in delta.changes:
    #     print("{} changed from {} to {}".format(change.field, change.old, change.new))

    # move the changereason into the history
    history_list_display.remove('changereason')
    def save_model(self, request, obj, form, change):
        if change:
            obj.changeReason = obj.changereason
            obj.changereason = '' # so the log message isn't reused next time
        super().save_model(request, obj, form, change)

admin.site.register(Trait, TraitAdmin)
