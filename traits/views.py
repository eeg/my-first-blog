from django.views.generic import CreateView, TemplateView
from django.urls import reverse_lazy
from .models import Trait

class TraitCreateView(CreateView):
    model = Trait
    fields = ('genus', 'species', 'breeding_system', 'isi')
    success_url = reverse_lazy('traits_success')
    template_name = 'traits/create.html'

class TraitSuccessView(TemplateView):
    template_name = 'traits/success.html'
