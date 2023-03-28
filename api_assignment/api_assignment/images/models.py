from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    Basic = 'basic'
    Premium = 'premium'
    Enterprise = 'enterprise'

    USER_PLAN_CHOICES = (
        (Basic, 'A link to a thumbnail that is 200px in height'),
        (Premium, 'A link to a thumbnail that is 200px, 400px in height and a link to the originally uploaded image'),
        (Enterprise, 'A link to a thumbnail that is 200px, 400px in height and a link to the originally uploaded '
                     'image. Ability to fetch a link for a previously uploaded image that expires after a number of '
                     'seconds (user can specify any number between 300 and 30000)'),
    )
    user = models.ForeignKey(User, models.CASCADE)
    user_plan = models.CharField(max_length=11, choices=USER_PLAN_CHOICES)
    image_pixel_size = models.PositiveIntegerField(default=200)


class Image(models.Model):
    title = models.CharField(max_length=200, blank=True)
    image = models.ImageField(upload_to='uplaod_images', blank=True)
    plan = models.ForeignKey(Profile, models.CASCADE)
    user = models.ForeignKey(User, models.CASCADE)
    url = models.URLField(null=True, blank=True)
