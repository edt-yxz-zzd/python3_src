"""mzitu_com_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import RedirectView
from .StaticImageView import StaticImageView


urlpatterns = [
    path('admin/', admin.site.urls),

    #new:
    re_path(r'(?=old/|all/|new/)', include('all_app.urls')),
    #path('old/', include('all_app.urls')),
    #path('all/', include('all_app.urls')),
    path('per/', include('per_app.urls')),
    re_path(r'echo_image/', include('proxy_app.urls')),
    path(r'index/', include('main_index_app.urls')),
    #path(r'/', include('main_index_app.urls')),
    path(r'', include('main_index_app.urls')),
    #re_path(r'(index/){0,1}\Z', include('main_index_app.urls')),
    #   SHOULD AVOID $

    #re_path(r'^favicon[.]ico$', RedirectView.as_view(url='/static/images/favicon.ico')),
        # https://stackoverflow.com/questions/9371378/warning-not-found-favicon-ico
        #   url(r'^favicon\.ico$', RedirectView.as_view(url='/static/images/favicon.ico')),
        #
        # https://stackoverflow.com/questions/47947673/is-it-better-to-use-path-or-url-in-urls-py-for-django-2-0?rq=1
        #   use "re_path()" instead of "url()"
        #
        # I draw "favicon.ico" by "Greenfish Icon Editor Pro"
        #
    #bug: this is not a relative path
    #   re_path(r'^favicon[.]ico$', StaticImageView('/static/images/favicon.ico')),
    #                                               ^^^

    re_path(r'^favicon[.]ico$', StaticImageView('static/images/favicon.ico'))
    #                                           ^^^ no "/" at beginning
    if 0 else re_path(r'^favicon[.]ico$', RedirectView.as_view(url='/static/images/favicon.ico')),
]
