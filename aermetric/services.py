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


class StatisticService:
    @classmethod
    def get_statistics(cls):
        try:
            annotate_args = {
                'info_count': Sum('info_count'),
                'errors_count': Sum('errors_count'),
                'lower_a': Count('id', filter=Q(type='Lower A')),
                'lower_b': Count('id', filter=Q(type='Lower B')),
                'paired_a': Count('id', filter=Q(type='Paired A')),
                'paired_b': Count('id', filter=Q(type='Paired B')),
                'upper_a': Count('id', filter=Q(type='Upper A')),
                'preLegend': Count('id', filter=Q(type='PreLegend')),
                'legend': Count('id', filter=Q(type='Legend')),
                'repeat_legend': Count('id', filter=Q(type='Repeat Legend')),
                'warning': Count('id', filter=Q(type='Warning'))
            }

            status_query = AircraftStatData.objects.values('status').annotate(
                **annotate_args
            )
            aircraft_query = AircraftStatData.objects.values('aircraft').annotate(
                **annotate_args
            )
            type_query = AircraftStatData.objects.values('type').annotate(
                **annotate_args
            )
            mix_query = chain(aircraft_query, status_query, type_query)

        except Exception as e:
            raise GenerateStatisticException(f'Something wrong with generate statistic query , error: {e}')
        return mix_query
