from django.conf.urls import url
from traits.views import TraitCreateView, TraitSuccessView

urlpatterns = [
    url(r'^traits/create/$', TraitCreateView.as_view(), name='traits_create'),
    url(r'^traits/success/$', TraitSuccessView.as_view(), name='traits_success'),
]
