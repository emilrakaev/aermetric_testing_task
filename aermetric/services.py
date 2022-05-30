from django.core.files.base import ContentFile
from django.core.files.storage import FileSystemStorage
from aermetric.models import AircraftErrorData
import csv


class UploadFileService:
    @classmethod
    def parse_file_and_upload_in_model(cls, file):
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

        product_list = []

        for id_, row in enumerate(reader):
            (
                priority,
                type,
                aircraft,
                status,
                errors_count,
                info_count
            ) = row

            product_list.append(
                AircraftErrorData(
                    priority=priority,
                    type=type,
                    aircraft=aircraft,
                    status=status,
                    errors_count=errors_count,
                    info_count=info_count,
                )
            )

        AircraftErrorData.objects.bulk_create(product_list)
