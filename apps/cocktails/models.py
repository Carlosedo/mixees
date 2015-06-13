from django.db import models


class Cocktail(models.Model):
    title = models.CharField(max_length=80, unique=True)
    slug = models.SlugField(max_length=80, unique=True)
    description = models.TextField()
    views = models.IntegerField(default=0)

    class Meta:
        verbose_name = "Cocktail"
        verbose_name_plural = "Cocktails"

    def __unicode__(self):
        return self.title

    @models.permalink
    def get_absolute_url(self):
        return ('cocktail_detail', [self.slug])

    