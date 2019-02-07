

'''
https://stackoverflow.com/questions/34564579/read-static-file-in-view

django.conf.settings.BASE_DIR/STATIC_ROOT
    #XXX_project.settings:
        #BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        #STATIC_ROOT = os.path.join(BASE_DIR, 'static')

'''

######################################
from django.conf import settings
from django.http import HttpResponse, StreamingHttpResponse
from django.core.files.storage import get_storage_class
import os.path
import imghdr

class StaticImageView:
    '''

# .../urls.py
urlpatterns = [
    ...
    re_path(r'^favicon[.]ico$', StaticImageView('static/images/favicon.ico')),
    #                                           ^^^ no "/" at beginning
    ...
]

'''
    def __init__(self, relative_path):
        self.relative_path = relative_path
        self.path = os.path.join(settings.BASE_DIR, self.relative_path)
        #print('path =', self.path)
        #print('BASE_DIR =', settings.BASE_DIR)
        #print('relative_path =', relative_path)

    def __call__(self, request):
        if request.method == 'GET':
            storage_class = get_storage_class(settings.STATICFILES_STORAGE)
            image_file = storage_class().open(self.path)
            #https://stackoverflow.com/questions/16252656/django-content-type-of-an-image-file
            file_type = imghdr.what(image_file)
            content_type = f'image/{file_type}'
            return StreamingHttpResponse(image_file, content_type=content_type)

            image_file = storage_class().open(self.path)
            return StreamingHttpResponse(image_file, content_type='image/jpeg')

            image_data = image_file.read()
            return HttpResponse(image_data, content_type='image/jpeg')

