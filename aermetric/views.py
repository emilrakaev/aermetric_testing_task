from rest_framework.generics import GenericAPIView

from rest_framework.response import Response
from rest_framework import status

from aermetric.serializers import FileFieldSerializer
from aermetric.services import UploadFileService


class UploadData(GenericAPIView):

    def post(self, request, *args, **kwargs):
        file = request.FILES['file']

        UploadFileService.parse_file_and_upload_in_model(file)

        return Response("Successfully upload the data", status=status.HTTP_201_CREATED)
