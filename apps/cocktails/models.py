from django.db import models
from django.template.defaultfilters import slugify


class Cocktail(models.Model):
    title = models.CharField(max_length=80, unique=True)
    slug = models.SlugField(max_length=80, unique=True)
    description = models.TextField()
    views = models.IntegerField(default=0)

    class Meta:
        verbose_name = "Cocktail"
        verbose_name_plural = "Cocktails"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Cocktail, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.title

    @models.permalink
    def get_absolute_url(self):
        return ('cocktail_detail', [self.slug])

