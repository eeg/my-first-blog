from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from traits.admin import TraitInline
from .models import Pub
from .resources import PubResource

class PubAdmin(ImportExportModelAdmin):
    inlines = [
        TraitInline,
    ]
    resource_class = PubResource

    list_display = ('citekey', 'author') # get error if trying to include all fields
    search_fields = ('citekey', 'author')

admin.site.register(Pub, PubAdmin)
