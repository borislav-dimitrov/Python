import PIL
from django.contrib.auth.models import User
from django.db import models

class profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # default='2021/02/11/default.jpg', upload_to='%Y/%m/%d/'
    picture = models.ImageField(default='2021/02/11/default.jpg', upload_to='%Y/%m/%d/', max_length=255, null=True,
                                blank=True)
    # Users may have multiple birthdays
    birthDate = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.user.username

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if self.picture:
            img = PIL.Image.open(self.picture.path)

            if img.height > 300 or img.width > 300:
                output_size = (300, 300)
                img.thumbnail(output_size)
                img.save(self.picture.path)
