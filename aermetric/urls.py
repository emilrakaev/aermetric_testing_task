from django.urls import path

from aermetric.views import UploadData

urlpatterns = [
    path('upload_data/', UploadData.as_view(), name='upload_data'),
]
