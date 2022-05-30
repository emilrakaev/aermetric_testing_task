from rest_framework import status as rest_status, status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from aermetric.serializers import AircraftStatDataSerializer
from aermetric.services import UploadFileService, StatisticService


class UploadData(GenericAPIView):
    def post(self, request, *args, **kwargs):
        try:
            file = request.FILES['file']
            UploadFileService.parse_file_and_upload_in_model(file)
        except Exception as e:
            return Response(data={f"Error": f"{str(e)}"}, status=status.HTTP_400_BAD_REQUEST)

        return Response("Successfully upload the data", status=rest_status.HTTP_201_CREATED)


class GetStatistics(GenericAPIView):
    serializer_class = AircraftStatDataSerializer

    def get(self, request, *args, **kwargs):
        try:
            result = StatisticService.get_statistics()
        except Exception as e:
            return Response(data={f"Error": f"{str(e)}"}, status=status.HTTP_400_BAD_REQUEST)

        return Response(self.serializer_class(result, many=True).data)
