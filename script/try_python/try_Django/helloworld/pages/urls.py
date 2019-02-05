# pages/urls.py
from django.urls import path

from . import views
urlpatterns = [
    # regular expression of path: ''
    # an optional url name: 'home'
    path('', views.homePageView, name='home')
]
