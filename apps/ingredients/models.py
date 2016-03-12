from django.db import models
from django.core.validators import MaxValueValidator
from django.template.defaultfilters import slugify
# from django.contrib.contenttypes import generic
# from django.contrib.contenttypes.models import ContentType

from apps.cocktails.models import Cocktail


class Liquid(models.Model):
    """Base class for Spirit and Mixer"""
    name = models.CharField(max_length=20, unique=True)
    slug = models.CharField(max_length=20, unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Liquid, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        abstract = True


class Spirit(Liquid):
    volume = models.PositiveSmallIntegerField(null=True, validators=[MaxValueValidator(100)])

    class Meta:
        verbose_name = "Spirit"
        verbose_name_plural = "Spirits"

    @property
    def volume_display(self):
        return "%g%%" % self.volume

    @models.permalink
    def get_absolute_url(self):
        return ('spirit_detail', [self.slug])


class Mixer(Liquid):
    class Meta:
        verbose_name = "Mixer"
        verbose_name_plural = "Mixers"

    @models.permalink
    def get_absolute_url(self):
        return ('mixer_detail', [self.slug])


class Ingredient(models.Model):
    """Ingredient class is the join for Cocktails and Liquids"""
    cocktail = models.ForeignKey(Cocktail)
    amount = models.DecimalField(decimal_places=2, max_digits=5, null=True)
    measurement = models.CharField(default='Some', max_length=30)
    spirit = models.ForeignKey(Spirit, blank=True, null=True)
    mixer = models.ForeignKey(Mixer, blank=True, null=True)

    class Meta:
        verbose_name = "Ingredient"
        verbose_name_plural = "Ingredients"

    def save(self, *args, **kwargs):
        if self.spirit:
            self.cocktail.total_parts += self.amount
            self.cocktail.save()

        super(Ingredient, self).save(*args, **kwargs)

    def __str__(self):
        if self.amount:
            return "%g %s" % (self.amount, self.measurement)
        else:
            return self.measurement


