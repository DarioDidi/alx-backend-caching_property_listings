'''
     getallproperties() function that:

    Checks Redis for all_properties using cache.get('all_properties').
    FetchesProperty.objects.all() if not found.
    Stores the queryset in Redis with 
    cache.set('all_properties', queryset, 3600)
    Returns the queryset.
'''

from django.core.cache import cache

from .models import Property


def getallproperties():
    queryset = cache.get('all_properties')
    if not queryset:
        queryset = Property.objects.all()
        cache.set('all_properties', queryset, 3600)

    return queryset
