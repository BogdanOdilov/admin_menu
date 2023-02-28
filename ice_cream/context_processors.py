from django.core.cache import cache
from settings import MYMENU_CACHE_KEY, MYMENU_CACHE_TIMEOUT

import models


def context(request):
    cached_menus = cache.get(MYMENU_CACHE_KEY)
    if cached_menus is not None:
        return cached_menus
    menus = models.Menu.objects.filter()
    context = {'menu': {}}
    for menu in menus:
        context['menu'][menu.slug] = menu
    cache.set(MYMENU_CACHE_KEY, context, MYMENU_CACHE_TIMEOUT)
    return context
