from factory import SubFactory
from factory.django import DjangoModelFactory

from images.models import User, Profile


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
