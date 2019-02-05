from django.shortcuts import render

# Create your views here.

#new:
from django.http import HttpResponse
from mzitu_com_project.DATA import (
    website_per_page_url_tpl
    ,per_page_url_regex
    )
from mzitu_com_project.per_page_transform import per_page_transform__url


def per_mzitu__page_view(request):
    path = request.path.lower()
    m = per_page_url_regex.fullmatch(path)
    if m is None: raise Exception(path)
    str_NUMBER = m['NUMBER']
    old_url = 'https://' + website_per_page_url_tpl.format(NUMBER=str_NUMBER)
    per_page = per_page_transform__url(old_url)
    return HttpResponse(per_page)

