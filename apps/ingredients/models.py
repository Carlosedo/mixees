from django.db import models
from django.core.validators import MaxValueValidator
# from django.contrib.contenttypes import generic
# from django.contrib.contenttypes.models import ContentType


from apps.cocktails.models import Cocktail

MEASUREMENT_CHOICES = (
    (1, "ml"),
    (2, "oz"),
    (3, "cup"),
    (4, "part"),
    (5, "teaspoon"),
)


class Liquid(models.Model):
    """Base class for Spirit and Mixer"""
    name = models.CharField(max_length=20, unique=True)
    slug = models.CharField(max_length=20, unique=True)
    
    def __unicode__(self):
        return self.name  


class Spirit(Liquid):
    volume = models.PositiveSmallIntegerField(validators=[MaxValueValidator(100)])

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
    """Base class for mixers and spirits"""
    cocktail = models.ForeignKey(Cocktail)
    amount = models.DecimalField(decimal_places=2, max_digits=5, null=True)
    measurement = models.SmallIntegerField(choices=MEASUREMENT_CHOICES)
    liquid = models.ForeignKey(Liquid)

    # models that can be linked to the generic foreign key
    # limit = models.Q(app_label='ingredients', model='Spirit') | \
    #     models.Q(app_label='ingredients', model='Mixer')
    # content_type = models.ForeignKey(
    #     ContentType,
    #     limit_choices_to=limit,
    #     null=True,
    #     blank=True,
    # )
    # object_id = models.PositiveIntegerField(null=True)
    # liquid = generic.GenericForeignKey('content_type', 'object_id')

    class Meta:
        verbose_name = "Ingredient"
        verbose_name_plural = "Ingredients"
    
    def __unicode__(self):
        return "%g %s" % (self.amount, self.get_measurement_display())
        

# class SpiritIngredient(Ingredient):
#     spirits = models.ForeignKey(Spirit)

#     class Meta:
#         verbose_name = "Ingredient"
#         verbose_name_plural = "Ingredients"


# class MixerIngredient(Ingredient):
#     mixers = models.ForeignKey(Mixer)

#     class Meta:
#         verbose_name = "Mixer Ingredient"
#         verbose_name_plural = "Mixer Ingredients"

