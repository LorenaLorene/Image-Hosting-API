from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from .factories import ProfileFactory
from parameterized import parameterized
from PIL import Image
import io

from django.core.files.base import ContentFile

API_ADDRESS = "http://localhost:8000/"


def generate_photo_file():
    image_file = io.BytesIO()
    image = Image.new('RGBA', size=(50, 50), color=(256, 0, 0))
    image.save(image_file, 'png')
    image_file.seek(0)

    django_friendly_file = ContentFile(image_file.read(), 'test.png')
    return django_friendly_file


def generate_post_data(profile):
    data = {
        "title": "Hello",
        "image": generate_photo_file(),
        "plan": profile
    }
    return data


basic_profile = ProfileFactory.create(user_plan="basic")
premium_profile = ProfileFactory.create(user_plan='premium')
enterprise_profile = ProfileFactory.create(user_plan='enterprise')


class ImageUploadTestCase(APITestCase):

    @classmethod
    def setUpTestData(cls):
        cls.client = APIClient()

    @parameterized.expand(
        [
            [generate_post_data(basic_profile), status.HTTP_201_CREATED],
            [generate_post_data(premium_profile), status.HTTP_201_CREATED],
            [generate_post_data(enterprise_profile), status.HTTP_201_CREATED],
        ]
    )
    def test_image_upload(self, data, status_code):
        response = self.client.post(path=API_ADDRESS + "upload_images/",
                                    data=data)
        self.assertEqual(response.status_code, status_code)
