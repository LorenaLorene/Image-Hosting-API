from factory import SubFactory
from factory.django import DjangoModelFactory
from django.contrib.auth.models import User
from images.models import Profile


class UserFactory(DjangoModelFactory):
    email = "lorenijo@gmail.com"
    password = "FakePassword123"

    class Meta:
        model = User


class ProfileFactory(DjangoModelFactory):
    user = SubFactory(UserFactory)
    user_plan = "basic"

    class Meta:
        model = Profile
