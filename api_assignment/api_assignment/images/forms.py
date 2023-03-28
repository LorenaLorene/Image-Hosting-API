# -*- coding: utf-8 -*-
from django import forms
from .models import Image, Profile
from PIL import Image
import io


def resize_image(image_field, size_measures):
    if image_field:
        try:
            image_file = io.BytesIO(image_field.file.read())
            image = Image.open(image_file)
            image.thumbnail(size_measures, Image.ANTIALIAS)
            image_file = io.BytesIO()
            image.save(image_file, 'PNG')
            image_field.file = image_file
            image_field.image = image

            return image_field
        except IOError:
            print("Error during resize image")


# class ImageForm(forms.ModelForm):
#     """Form for the image model that will resize uploaded image based on account plan"""
#
#     def get_user_plan(self, request):
#         user = request.user
#         user_plan = getattr(Profile.objects.get(user=user), 'user_plan')
#         return user_plan
#
#     def resize_image(self):
#         image_field = self.cleaned_data.get('image')
#         user_plan = self.get_user_plan()
#         if user_plan == 'basic':
#             resize_image(image_field, (200, 200))
#         elif user_plan == 'premium':
#             resize_image(image_field, (400, 400))
#         elif user_plan == 'enterprice':
#             resize_image(image_field, (200, 200))
#
#     class Meta:
#         model = Image
#         fields = ('title', 'image', 'plan')
