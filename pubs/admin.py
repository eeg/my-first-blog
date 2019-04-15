from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from traits.admin import TraitInline
from .models import Pub, Person
from .resources import PubResource, PersonResource

class PubAdmin(ImportExportModelAdmin):
    inlines = [
        TraitInline, # all Traits associated with this Pub
    ]
    resource_class = PubResource

class PersonAdmin(ImportExportModelAdmin):
    resource_class = PersonResource

admin.site.register(Pub, PubAdmin)
admin.site.register(Person, PersonAdmin)
