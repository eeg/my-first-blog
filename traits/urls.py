from django.conf.urls import url
from traits.views import TraitCreateView

urlpatterns = [
    url(r'^traits/create/$', TraitCreateView.as_view(), name="create_trait"),
]
