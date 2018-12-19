from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from .models import Trait

class TraitForm(forms.ModelForm):
    class Meta:
        model = Trait
        fields = ('genus', 'species', 'isi', 'breeding_system')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save trait record'))
