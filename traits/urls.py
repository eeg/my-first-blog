from django.conf.urls import url
from traits.views import TraitCreateView, TraitSuccessView

urlpatterns = [
    #url(r'^traits/create/$', TraitCreateView.as_view(success_url='.'), name='traits_create'), # return to same page
    url(r'^traits/create/$', TraitCreateView.as_view(success_url='../success'), name='traits_create'), # go to traits/success/
    url(r'^traits/success/$', TraitSuccessView.as_view(), name='traits_success'),
]
