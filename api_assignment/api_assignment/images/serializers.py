from rest_framework import serializers
from django.contrib.auth.models import User
from images.models import Image, Profile


class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        exclude = ['basic_thumbnail_height', "premium_thumbnail_height", "user_plan"]


class ImageSerializer(serializers.ModelSerializer):
    title = serializers.CharField(allow_null=True, required=False)
    image = serializers.ImageField()

    class Meta:
        model = Image
        exclude = ['plan']
