from django.db import models
from django.contrib.auth.models import AbstractBaseUser, UserManager, PermissionsMixin


class User(AbstractBaseUser, PermissionsMixin):
    """
        An abstract base class implementing a fully featured User model with
        admin-compliant permissions.
        Email, password and user_plan are required. Other fields are optional.
    """
    username = models.CharField(max_length=30, blank=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    email = models.EmailField(unique=True,)
    is_staff = models.BooleanField(default=False)  #a admin user; non super-user
    is_superuser = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']


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
    user = models.OneToOneField(User, models.CASCADE)
    user_plan = models.CharField(max_length=11, choices=USER_PLAN_CHOICES)
    basic_thumbnail_height = models.PositiveIntegerField(default=200)
    premium_thumbnail_height = models.PositiveIntegerField(default=400)
    url = models.URLField(null=True, blank=True)


class Image(models.Model):
    title = models.CharField(max_length=200, blank=True)
    image = models.ImageField(upload_to='uplaod_images', blank=True)
    plan = models.ForeignKey(Profile, models.CASCADE)
    user = models.ForeignKey(User, models.CASCADE)
