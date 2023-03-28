from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from django.contrib.auth.models import User
from images.models import Profile
from images.serializers import ProfileSerializer, ImageSerializer
# from images.forms import ImageForm
from rest_framework.response import Response
from rest_framework import status


class GetImagesListView(ListAPIView):
    """
    List images
    """

    serializer_class = ProfileSerializer

    def get_queryset(self):
        user = self.request.user
        return Profile.objects.filter(user=user)


class ImageUploadView(APIView):
    """Process images uploaded by users"""

    serializer_class = ImageSerializer

    @staticmethod
    def upload_image(request):
        if request.method == 'POST':
            # form = ImageForm(request.POST, request.FILES)
            # if form.is_valid():
            #     form.save()
                return Response(request.data, status=status.HTTP_201_CREATED)
            # else:
            #     # form = ImageForm()
            #     return Response(status=status.HTTP_400_BAD_REQUEST)
