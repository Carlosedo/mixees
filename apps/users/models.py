from django.db import models
from django.contrib.auth.models import User

from apps.cocktails.models import Cocktail


class UserProfile(models.Model):
    """Default user profile for Mixees """
    user = models.OneToOneField(User)

    twitter = models.URLField(blank=True)
    facebook = models.URLField(blank=True)
    image = models.ImageField(upload_to='profile_images', blank=True)
    liked_cocktails = models.ManyToManyField(Cocktail, blank=True)

    def __unicode__(self):
        return self.user.username
