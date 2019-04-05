from import_export import fields, resources
from import_export.widgets import ForeignKeyWidget
from .models import Trait, Publocal

# within Meta, could also...
#   specify which fields to import/export
#   order the fields in the export file

class TraitResource(resources.ModelResource):
    pubref = fields.Field(
                column_name = 'pubref',
                attribute = 'pubref',
                widget = ForeignKeyWidget(Publocal, 'citekey')
            )

    class Meta:
        model = Trait
        #  report_skipped = True
        #  skip_unchanged = True

class PublocalResource(resources.ModelResource):
    class Meta:
        model = Publocal
        #  import_id_fields = ('citekey')
