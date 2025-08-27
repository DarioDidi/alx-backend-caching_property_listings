from django.core.cache import cache

from .models import Property


def getallproperties():
    queryset = cache.get('all_properties')
    if not queryset:
        queryset = Property.objects.all()
        cache.set('all_properties', queryset, 3600)

    return queryset
