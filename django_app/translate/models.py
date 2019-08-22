from django.db import models


class Country(models.Model):
    iso = models.CharField(max_length=2, unique=True)

    def __str__(self):
        return self.iso


class Bahasa(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text


class ForeignTranslation(models.Model):
    bahasa = models.ForeignKey(Bahasa, related_name='translations', on_delete=models.CASCADE)
    country = models.ForeignKey(Country, related_name='translations', on_delete=models.CASCADE)
    text = models.TextField()

    def __str__(self):
        return "foreign: ({}) <> bahasa: ({}) <> ({})".format(
            self.text, self.bahasa, self.country
        )
