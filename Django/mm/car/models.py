from django.db import models
from django.utils import timezone


# Is branding a brand or a model
class Brand(models.Model):
    name = models.CharField(max_length=200)
    image = models.CharField(max_length=500, blank=True, null=True)
    year_established = models.DateField(default=timezone.now().year)

    def __str__(self):
        return '1'

# or the brand is model
class Model(models.Model):
    name = models.CharField(max_length=200)
    image = models.CharField(max_length=500, blank=True, null=True)
    description = models.CharField(max_length=500, blank=True, null=True)
    brand = models.ForeignKey(Brand, related_name="model", on_delete=models.CASCADE)

# Should rating be modeled as a brand?
class Rating(models.Model):
    rating = models.IntegerField()
class Comment(models.Model):
    comment = models.CharField(max_length=750)
    owner = models.ForeignKey('auth.User', related_name='comments', on_delete=models.CASCADE)
    rating = models.ManyToManyField(Rating, blank=True, null=True)
