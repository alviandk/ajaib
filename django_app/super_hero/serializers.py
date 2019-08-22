from rest_framework import serializers

from .models import (
    Address,
    City,
    Country,
    Gender,
    Hero,
    Power
)


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = "__all__"


class CitySerializer(serializers.ModelSerializer):
    country = CountrySerializer(read_only=True)

    class Meta:
        model = City
        fields = "__all__"


class CitySerializerAlter(serializers.ModelSerializer):

    class Meta:
        model = City
        fields = "__all__"


class AddressSerializer(serializers.ModelSerializer):
    city = CitySerializer(read_only=True)

    class Meta:
        model = Address
        fields = "__all__"


class AddressSerializerAlter(serializers.ModelSerializer):

    class Meta:
        model = Address
        fields = "__all__"


class GenderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gender
        fields = "__all__"


class PowerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Power
        fields = "__all__"


class HeroSerializer(serializers.ModelSerializer):
    gender = GenderSerializer(read_only=True)
    power = PowerSerializer(many=True, read_only=True)
    address = AddressSerializer(many=True, read_only=True)

    class Meta:
        model = Hero
        fields = "__all__"


class HeroSerializerAlter(serializers.ModelSerializer):

    class Meta:
        model = Hero
        fields = "__all__"
