from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views
from rest_framework import renderers


address_list = views.AddressViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
address_detail = views.AddressViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})
city_list = views.CityViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
city_detail = views.CityViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})
country_list = views.CountryViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
country_detail = views.CountryViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})
gender_list = views.GenderViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
gender_detail = views.GenderViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})
hero_list = views.HeroViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
hero_detail = views.HeroViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})
hero_post = views.HeroViewSetAlter.as_view({
    'post': 'create'
})
hero_edit = views.HeroViewSetAlter.as_view({
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})
power_list = views.PowerViewSet.as_view({
    'get': 'list',
})
power_detail = views.PowerViewSet.as_view({
    'get': 'retrieve',
})


urlpatterns = format_suffix_patterns([
    path('', views.api_root),
    path('address/', address_list, name='address-list'),
    path('address/<int:pk>/', address_detail, name='address-detail'),
    path('city/', city_list, name='city-list'),
    path('city/<int:pk>/', city_detail, name='city-detail'),
    path('country/', country_list, name='country-list'),
    path('country/<int:pk>/', country_detail, name='country-detail'),
    path('gender/', gender_list, name='gender-list'),
    path('gender/<int:pk>/', gender_detail, name='gender-detail'),
    path('hero/', hero_post, name='hero-post'),
    path('hero/<int:pk>/edit/', hero_edit, name='hero-edit'),
    path('hero/all/', hero_list, name='hero-list'),
    path('hero/<int:pk>/', hero_detail, name='hero-detail'),
    path('power/', power_list, name='power-list'),
    path('power/<int:pk>/', power_detail, name='power-detail'),
])
