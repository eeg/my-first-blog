from django.views.generic import CreateView
from .models import Trait

class TraitCreateView(CreateView):
    model = Trait
    fields = ('genus', 'species', 'breeding_system', 'isi')
    template_name = 'traits/create_trait.html'
