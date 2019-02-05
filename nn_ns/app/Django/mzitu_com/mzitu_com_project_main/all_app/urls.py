# pages/urls.py
from django.urls import path, re_path

#from .views import homePageView
from .views import all_old_mzitu__page_view, all_new_mzitu__page_view
urlpatterns = [
    #path('', homePageView, name='home'),
    path('old/', all_old_mzitu__page_view, name='all_old'),
    path('all/', all_new_mzitu__page_view, name='all_new'),
    path('new/', all_new_mzitu__page_view, name='all_new'),
]
