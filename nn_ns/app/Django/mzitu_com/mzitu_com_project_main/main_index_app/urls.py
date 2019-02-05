# pages/urls.py
from django.urls import path, re_path

from .views import mainPageView
urlpatterns = [
    path('', mainPageView, name='main_index'),
]
