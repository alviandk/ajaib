from django.contrib import admin
from .models import (
    Address,
    City,
    Country,
    Gender,
    Hero,
    Power
)


admin.site.register(Address)
admin.site.register(City)
admin.site.register(Country)
admin.site.register(Gender)
admin.site.register(Hero)
admin.site.register(Power)
