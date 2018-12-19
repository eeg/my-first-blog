from django.conf.urls import url
from traits.views import TraitCreateView, TraitSuccessView, TraitUpdateView

urlpatterns = [
    url(r'^traits/create/$', TraitCreateView.as_view(), name='traits_create'),
    url(r'^traits/success/$', TraitSuccessView.as_view(), name='traits_success'),
    url(r'^traits/update/(?P<pk>\d+)/$', TraitUpdateView.as_view(), name='traits_update'),
]
