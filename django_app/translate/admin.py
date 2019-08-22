from django.contrib import admin

from .models import Country, Bahasa, ForeignTranslation


admin.site.register(Country)
admin.site.register(Bahasa)


@admin.register(ForeignTranslation)
class ForeignTranslationAdmin(admin.ModelAdmin):
    list_display = ('country', 'bahasa', 'text')
    list_editable = ('text',)
