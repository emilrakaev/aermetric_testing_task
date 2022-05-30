import csv
from itertools import chain

from django.core.files.base import ContentFile
from django.core.files.storage import FileSystemStorage
from django.db.models import Sum, Count, Q

from aermetric.exceptions import FileParseException, GenerateStatisticException
from aermetric.models import AircraftStatData


class UploadFileService:
    @classmethod
    def parse_file_and_upload_in_model(cls, file):
        try:
            fs = FileSystemStorage(location='tmp/')

            content = file.read()
            file_content = ContentFile(content)
            file_name = fs.save(
                "_tmp.csv", file_content
            )
            tmp_file = fs.path(file_name)

            csv_file = open(tmp_file, errors="ignore")
            reader = csv.reader(csv_file)
            next(reader)
            data_list = []

            for id_, row in enumerate(reader):
                (
                    priority,
                    type,
                    aircraft,
                    status,
                    errors_count,
                    info_count
                ) = row

                data_list.append(
                    AircraftStatData(
                        priority=priority,
                        type=type,
                        aircraft=aircraft,
                        status=status,
                        errors_count=errors_count,
                        info_count=info_count,
                    )
                )

            AircraftStatData.objects.bulk_create(data_list)
        except Exception as e:
            raise FileParseException(f'Something wrong with upload file, error: {e}')
