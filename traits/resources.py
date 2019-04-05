from import_export import resources
from .models import Trait, Publocal

# within Meta, could also...
#   specify which fields to import/export
#   order the fields in the export file

class TraitResource(resources.ModelResource):
    class Meta:
        model = Trait
        #  report_skipped = True
        #  skip_unchanged = True

class PublocalResource(resources.ModelResource):
    class Meta:
        model = Publocal
        #  import_id_fields = ('citekey')
