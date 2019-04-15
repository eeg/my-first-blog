from import_export import fields, resources
from import_export.widgets import ForeignKeyWidget
from .models import Pub, Person

# within Meta, could also...
#   specify which fields to import/export
#   order the fields in the export file

class PubResource(resources.ModelResource):

    class Meta:
        model = Pub
        #  import_id_fields = ('citekey')

    def before_import(self, dataset, using_transactions, dry_run=True, collect_failed_rows=False, **kwargs):
        if 'id' not in dataset.headers:
            dataset.insert_col(0, lambda row: '', header='id')

class PersonResource(resources.ModelResource):

    class Meta:
        model = Person
