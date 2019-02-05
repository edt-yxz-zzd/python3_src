from django.shortcuts import render

# Create your views here.

#new:
from django.http import HttpResponse
try:
    from ..mzitu_com_project.DATA import website_all_new, website_all_old
    from ..mzitu_com_project.home_page_transform import home_page_transform__url
except (ImportError, ValueError):
    from mzitu_com_project.DATA import website_all_new, website_all_old
    from mzitu_com_project.home_page_transform import home_page_transform__url

website_all_old = str(website_all_old)
website_all_new = str(website_all_new)

def all_old_or_new_mzitu__page_view(request, url):
    url = 'https://' + url
    page = home_page_transform__url(url)
    return HttpResponse(page)
    return HttpResponse(url)
def all_old_mzitu__page_view(request):
    return all_old_or_new_mzitu__page_view(request, website_all_old)
    return HttpResponse('all_old')
def all_new_mzitu__page_view(request):
    return all_old_or_new_mzitu__page_view(request, website_all_new)
    return HttpResponse('all_new')

'''
def homePageView(request):
    path = request.path.lower()
    assert path in ('/all/', '/old/')
    if path == '/all/':
        f = all_new_mzitu__page_view
    elif path == '/old/':
        f = all_old_mzitu__page_view
    else:
        return HttpResponse(f'logic-error: mzitu_com.all_app.homePageView : {__file__}')
    return f(request)


    print(request)
    print(repr(request))
    print(dir(request))
    for attr in dir(request):
        print(attr, '=', getattr(request, attr))

'''

