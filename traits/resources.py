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
        clean_model_instances = True
        #  fields = ('id', 'genus', 'species', 'isi', 'breeding_system', 'pubref')

        report_skipped = True
        skip_unchanged = True
        # "unchanged" applies to rows that are identical to existing ones, including 
        # the unique id and all other columns present in the imported file
        #     skip_changed = False: identical imported rows are recorded as updates
        #     skip_changed = True:  identical imported rows are skipped

    def before_import(self, dataset, using_transactions, dry_run=True, collect_failed_rows=False, **kwargs):
        if 'id' not in dataset.headers:
            dataset.insert_col(0, lambda row: '', header='id')

class PublocalResource(resources.ModelResource):

    class Meta:
        model = Publocal
        #  import_id_fields = ('citekey')

    def before_import(self, dataset, using_transactions, dry_run=True, collect_failed_rows=False, **kwargs):
        if 'id' not in dataset.headers:
            dataset.insert_col(0, lambda row: '', header='id')
