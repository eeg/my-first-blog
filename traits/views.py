from django.views.generic import CreateView, TemplateView, UpdateView
from django.urls import reverse_lazy
from .models import Trait
from .forms import TraitForm

# not using forms.py; fields specified here instead
class TraitCreateView(CreateView):
    model = Trait
    fields = ('genus', 'species', 'breeding_system', 'isi')
    success_url = reverse_lazy('traits_success')
    template_name = 'traits/create.html'

class TraitSuccessView(TemplateView):
    template_name = 'traits/success.html'

# using forms.py with formhelper; fields specified there
class TraitUpdateView(UpdateView):
    model = Trait
    form_class = TraitForm
    success_url = reverse_lazy('traits_success')
    template_name = 'traits/update.html'
