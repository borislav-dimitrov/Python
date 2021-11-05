from django.db import models
from django.utils import timezone

from car.models import Model

postPut = [('post', 'model'), ('put', 'model')]
PostDelete = [('post', 'model'), ('delete', 'model')]
get_put_get_put = [('get', 'model'), ('put', 'model')]
get_post = [('get', 'model'), ('post', 'model')]

methods_for_getting_big_serializer_request = (
    (postPut, PostDelete, get_post, get_put_get_put), (postPut, PostDelete, get_post, get_put_get_put))


class Type(models.Model):
    name = models.CharField(max_length=200, null=False)

    def __str__(self):
        return self.name


class Specification(models.Model):
    the_name_of_the_specificSpecification = models.CharField(max_length=200, null=False)
    description = models.CharField(max_length=250, null=True)
    type = models.ForeignKey(Type, on_delete=models.CASCADE)

    def __str__(self):
        return 'spec name'


class CarPostPicture(models.Model):
    src = models.CharField(max_length=500)
    is_default_picture = models.BooleanField()

    def __str__(self):
        return self.src


class CarPost(models.Model):
    model = models.ForeignKey(Model, on_delete=models.CASCADE)
    published = models.DateTimeField(timezone.now().year, auto_now_add=True)
    price = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    phone_number = models.CharField(max_length=20)
    owner = models.ForeignKey('auth.User', related_name='carposts', on_delete=models.CASCADE, default=1)
    photos = models.ManyToManyField(CarPostPicture)
    specifications = models.ManyToManyField(Specification, blank=True)

    def __str__(self):
        return f'{self.model.name} - {self.price}'
