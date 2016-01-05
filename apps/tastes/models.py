from django.db import models
from django.template.defaultfilters import slugify


class Taste(models.Model):
    title = models.CharField(max_length=80, unique=True)
    slug = models.SlugField(max_length=80, unique=True)
    views = models.IntegerField(default=0)

    class Meta:
        verbose_name = "Taste"
        verbose_name_plural = "Tastes"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        if self.views < 0:
            self.views = 0
        super(Taste, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.title
