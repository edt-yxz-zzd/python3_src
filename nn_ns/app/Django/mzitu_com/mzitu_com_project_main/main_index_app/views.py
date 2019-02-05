from django.shortcuts import render

# Create your views here.

#new:
from django.http import HttpResponse
try:
    from ..mzitu_com_project.DATA import main_index_page
except (ImportError, ValueError):
    from mzitu_com_project.DATA import main_index_page

def mainPageView(request):
    path = request.path.lower()
    #print(f'path = {path!r}')
    assert path in ('/', '/index/')
    return HttpResponse(main_index_page)

'''
def mainPageView(*args, **kwargs):
    print(args)
    print(kwargs)
    return HttpResponse(main_index_page)
'''



