from importlib.util import find_spec

from django.conf import settings
from django.contrib import admin
from django.urls import include, path, reverse_lazy
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url=reverse_lazy('home'))),
]

for app in settings.MENUICE_APPS:
    mod = app + '.urls'
    if find_spec(mod):
        urlpatterns += [path(app + '/', include(mod)), ]
