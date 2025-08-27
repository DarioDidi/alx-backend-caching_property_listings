from .utils import getallproperties

from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_cookie
from django.http import JsonResponse

from rest_framework.decorators import api_view


@cache_page(60 * 15)
@vary_on_cookie
@api_view(["GET"])
def property_list(request):
    content = {"properties": getallproperties()}
    return JsonResponse({"data": content})
