from django.core.cache import cache
from django_redis import get_redis_connection

from .models import Property

from django.core.cache import cache
import logging

# Set up logging
logger = logging.getLogger(__name__)


def getallproperties():
    queryset = cache.get('all_properties')
    if not queryset:
        queryset = Property.objects.all()
        cache.set('all_properties', queryset, 3600)

    return queryset


def get_redis_cache_metrics():

    try:
        redis_client = cache.client.get_client()
        info_data = redis_client.info('stats')

        keyspace_hits = info_data.get('keyspace_hits', 0)
        keyspace_misses = info_data.get('keyspace_misses', 0)

        total_accesses = keyspace_hits + keyspace_misses
        if total_accesses > 0:
            hit_ratio = keyspace_hits / total_accesses
        else:
            hit_ratio = 0.0

        metrics = {
            'keyspace_hits': keyspace_hits,
            'keyspace_misses': keyspace_misses,
            'hit_ratio': hit_ratio,
            'total_accesses': total_accesses
        }

        logger.info(
            "Redis Cache Metrics - Hits: %d, Misses: %d, Hit Ratio: %.4f",
            keyspace_hits, keyspace_misses, hit_ratio
        )
        return metrics

    except Exception as e:
        logger.error("Failed to retrieve Redis cache metrics: %s", str(e))
        return {'error': str(e)}


def tearDown(self):
    get_redis_connection("default").flushall()
