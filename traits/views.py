from django.views.generic import CreateView, TemplateView
from .models import Trait

class TraitCreateView(CreateView):
    model = Trait
    fields = ('genus', 'species', 'breeding_system', 'isi')
    template_name = 'traits/create.html'

class TraitSuccessView(TemplateView):
    template_name = 'traits/success.html'
