from django.urls import path

from aermetric.views import UploadData, GetStatistics

urlpatterns = [
    path('upload_file/', UploadData.as_view(), name='upload_data'),
    path('get_statistic/', GetStatistics.as_view(), name='get_error_stats'),
]
