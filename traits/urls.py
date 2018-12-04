from django.conf.urls import url
from traits.views import TraitCreateView, TraitSuccessView

urlpatterns = [
    #url(r'^traits/create/$', TraitCreateView.as_view(success_url='.'), name='create_trait'), # return to same page
    url(r'^traits/create/$', TraitCreateView.as_view(success_url='../success'), name='create_trait'), # go to traits/success/
    url(r'^traits/success/$', TraitSuccessView.as_view(), name='traits_success'),
]
