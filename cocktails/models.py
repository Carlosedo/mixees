from django.db import models

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
    	return ('spirit_detail', [self.name])


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
        return ('mixer_detail', [self.name])


class Cocktail(models.Model):
    title = models.CharField(max_length=80, unique=True)
    slug = models.SlugField(max_length=80, unique=True)
    description = models.TextField()

    class Meta:
        verbose_name = "Cocktail"
        verbose_name_plural = "Cocktails"

    def __unicode__(self):
        return self.title

    @models.permalink
    def get_absolute_url(self):
        return ('cocktail_detail', [self.slug])


MEASUREMENT_CHOICES = (
    (1, "ml"),
    (2, "oz"),
    (3, "cup"),
    (4, "part"),
    (5, "teaspoon"),
)


class Ingredient(models.Model):
    cocktail = models.ForeignKey(Cocktail)
    spirits = models.ForeignKey(Spirit)
    amount = models.DecimalField(decimal_places=2, max_digits=5)
    measurement = models.SmallIntegerField(choices=MEASUREMENT_CHOICES)

    class Meta:
        verbose_name = "Ingredient"
        verbose_name_plural = "Ingredients"

    def __unicode__(self):
        return "%g %s of %s." % (self.amount, self.get_measurement_display(), self.spirits)


class MixerIngredient(models.Model):
    cocktail = models.ForeignKey(Cocktail)
    mixers = models.ForeignKey(Mixer)
    amount = models.DecimalField(decimal_places=2, max_digits=5)
    measurement = models.SmallIntegerField(choices=MEASUREMENT_CHOICES)

    class Meta:
        verbose_name = "Miver Ingredient"
        verbose_name_plural = "Mixer Ingredients"

    def __unicode__(self):
        return "%g %s of %s." % (self.amount, self.get_measurement_display(), self.mixers)   
    