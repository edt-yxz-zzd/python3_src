# pages/urls.py
from django.urls import path, re_path

from .views import download_image_file_as_view
urlpatterns = [
    # query is part of HTTP URL
    #   but not part of Django URL
    #re_path(r'[?]url=.+$', download_image_file_as_view),
    path('', download_image_file_as_view),
]
