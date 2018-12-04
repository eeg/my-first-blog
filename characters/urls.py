from django.conf.urls import url
from characters.views import CreateFooView

urlpatterns = [
    url(r'^foo/create/$', CreateFooView.as_view(success_url='.'), name="create_foo"),
]
