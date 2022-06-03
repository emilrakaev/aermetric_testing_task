from rest_framework import status as rest_status, status
from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.response import Response

from aermetric.serializers import AircraftStatDataSerializer, UploadFileSerializer
from aermetric.services import UploadFileService, StatisticService


class UploadData(CreateAPIView):
    serializer_class = UploadFileSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        if not serializer.is_valid():
            return Response(data={
                'message': 'Invalid input',
                'errors': serializer.errors
            }, status=status.HTTP_406_NOT_ACCEPTABLE)

        file = serializer.validated_data['file']

        try:
            UploadFileService.parse_file_and_upload_in_model(file)
        except Exception as e:
            return Response(data={f"Error": f"{str(e)}"}, status=status.HTTP_400_BAD_REQUEST)

        return Response("Successfully upload the data", status=rest_status.HTTP_201_CREATED)


class GetStatistics(ListAPIView):
    serializer_class = AircraftStatDataSerializer

    def get_queryset(self):
        try:
            result = StatisticService.get_statistics()
        except Exception as e:
            return Response(data={f"Error": f"{str(e)}"}, status=status.HTTP_400_BAD_REQUEST)
        return result
