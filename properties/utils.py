from django.core.cache import cache
from django_redis import get_redis_connection

from .models import Property

import logging

logger = logging.getLogger(__name__)


def get_all_properties():
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

        """if total_requests > 0 else 0"""
        total_requests = keyspace_hits + keyspace_misses
        if total_requests > 0:
            hit_ratio = keyspace_hits / total_requests
        else:
            hit_ratio = 0

        metrics = {
            'keyspace_hits': keyspace_hits,
            'keyspace_misses': keyspace_misses,
            'hit_ratio': hit_ratio,
            'total_requests': total_requests
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
