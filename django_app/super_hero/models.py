from django.db import models


class Country(models.Model):
    name = models.CharField(max_length=128, unique=True)

    def __str__(self):
        return self.name


class City(models.Model):
    name = models.CharField(max_length=128, unique=True)
    country = models.ForeignKey(
        Country,
        related_name='cities',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return "{} - {}".format(self.name, self.country)


class Address(models.Model):
    street_name = models.CharField(max_length=128, unique=True)
    city = models.ForeignKey(
        City,
        related_name='adresses',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return "{} - {}".format(self.street_name, self.city)


class Gender(models.Model):
    name = models.CharField(max_length=16, unique=True)

    def __str__(self):
        return self.name


class Power(models.Model):
    name = models.CharField(max_length=128, unique=True)

    def __str__(self):
        return self.name


class Hero(models.Model):
    full_name = models.CharField(max_length=128, unique=True)
    gender = models.ForeignKey(
        Gender,
        related_name='heroes',
        on_delete=models.CASCADE
    )
    power = models.ManyToManyField(
        Power,
        related_name='heroes'
    )
    address = models.ManyToManyField(Address, related_name='heroes')

    def __str__(self):
        return self.full_name
