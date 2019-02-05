# pages/urls.py
from django.urls import path, re_path

from .views import per_mzitu__page_view
urlpatterns = [
    re_path('\d+/$', per_mzitu__page_view),
]
