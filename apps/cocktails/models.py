from django.db import models
from django.template.defaultfilters import slugify

from apps.tastes.models import Taste

class Cocktail(models.Model):
    title = models.CharField(max_length=80, unique=True)
    slug = models.SlugField(max_length=80, unique=True)
    description = models.TextField(default='')
    total_parts = models.IntegerField(default=0)
    views = models.IntegerField(default=0)
    glass_type = models.CharField(max_length=80, null=True)
    mixing_instructions = models.TextField(default='')
    skill_level = models.CharField(max_length=80, null=True)
    # tastes = models.ManyToManyField(Taste)

    class Meta:
        verbose_name = "Cocktail"
        verbose_name_plural = "Cocktails"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)

        if self.views < 0:
            self.views = 0

        super(Cocktail, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    @models.permalink
    def get_absolute_url(self):
        return ('cocktail_detail', [self.slug])

