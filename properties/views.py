from .serializers import PropertySerializer
from .models import Property
from .utils import getallproperties()

# Create your views here.
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_cookie

from rest_framework.decorators import api_view
from rest_framework.response import Response


@cache_page(60 * 15)
@vary_on_cookie
@api_view(["GET"])
def property_list(request):
    content = {"properties": getallproperties()}
    return Response(content)
