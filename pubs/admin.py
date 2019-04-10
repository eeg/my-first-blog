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

admin.site.register(Pub, PubAdmin)
