from django.db import models

from apps.cocktails.models import Cocktail

MEASUREMENT_CHOICES = (
    (1, "ml"),
    (2, "oz"),
    (3, "cup"),
    (4, "part"),
    (5, "teaspoon"),
)


class Spirit(models.Model):
    name = models.CharField(max_length=20, unique=True)
    slug = models.CharField(max_length=20, unique=True)

    class Meta:
        verbose_name = "Spirit"
        verbose_name_plural = "Spirits"
    
    def __unicode__(self):
        return self.name

    @models.permalink
    def get_absolute_url(self):
        return ('spirit_detail', [self.slug])


class Mixer(models.Model):
    name = models.CharField(max_length=20, unique=True)
    slug = models.CharField(max_length=20, unique=True)

    class Meta:
        verbose_name = "Mixer"
        verbose_name_plural = "Mixers"

    def __unicode__(self):
        return self.name
        
    @models.permalink
    def get_absolute_url(self):
        return ('mixer_detail', [self.slug])


class Ingredient(models.Model):
    cocktail = models.ForeignKey(Cocktail)
    spirits = models.ForeignKey(Spirit)
    amount = models.DecimalField(decimal_places=2, max_digits=5)
    measurement = models.SmallIntegerField(choices=MEASUREMENT_CHOICES)

    class Meta:
        verbose_name = "Ingredient"
        verbose_name_plural = "Ingredients"

    def __unicode__(self):
        return "%g %s" % (self.amount, self.get_measurement_display())


class MixerIngredient(models.Model):
    cocktail = models.ForeignKey(Cocktail)
    mixers = models.ForeignKey(Mixer)
    amount = models.DecimalField(decimal_places=2, max_digits=5)
    measurement = models.SmallIntegerField(choices=MEASUREMENT_CHOICES)

    class Meta:
        verbose_name = "Miver Ingredient"
        verbose_name_plural = "Mixer Ingredients"

    def __unicode__(self):
        return "%g %s" % (self.amount, self.get_measurement_display())   


