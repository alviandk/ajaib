from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

from .models import (
    Address,
    City,
    Country,
    Gender,
    Hero,
    Power
)

from .serializers import (
    AddressSerializer,
    CitySerializer,
    CountrySerializer,
    GenderSerializer,
    HeroSerializer,
    HeroSerializerAlter,
    PowerSerializer
)


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'address': reverse('address-list', request=request, format=format),
        'city': reverse('city-list', request=request, format=format),
        'country': reverse('country-list', request=request, format=format),
        'power': reverse('power-list', request=request, format=format),
        'gender': reverse('gender-list', request=request, format=format),
        'hero': reverse('hero-list', request=request, format=format)
    })


class AddressViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = Address.objects.all()
    serializer_class = AddressSerializer


class CityViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = City.objects.all()
    serializer_class = CitySerializer


class CountryViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = Country.objects.all()
    serializer_class = CountrySerializer


class GenderViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = Gender.objects.all()
    serializer_class = GenderSerializer


class HeroViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = Hero.objects.all()
    serializer_class = HeroSerializer


class HeroViewSetAlter(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = Power.objects.all()
    serializer_class = HeroSerializerAlter


class PowerViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = Power.objects.all()
    serializer_class = PowerSerializer
