from django.test import TestCase

# Create your tests here.

#new:
from django.test import SimpleTestCase
try:
    from .mzitu_com_project._configure_ import using_StaticImageView_instead_of_RedirectView
except (ImportError, ValueError):
    from mzitu_com_project._configure_ import using_StaticImageView_instead_of_RedirectView

class SimpleTests(SimpleTestCase):
    '''
see: "README-url.txt"

http://127.0.0.1:8000/old/
http://127.0.0.1:8000/all/
    http://127.0.0.1:8000/new/
http://127.0.0.1:8000/index/
    http://127.0.0.1:8000/
http://127.0.0.1:8000/static/images/default_image.png
http://127.0.0.1:8000/static/images/favicon.ico
    http://127.0.0.1:8000/favicon.ico

'''
    def test_home_page_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
    def test_home_index_page_status_code(self):
        response = self.client.get('/index/')
        self.assertEqual(response.status_code, 200)
    def test_old_page_status_code(self):
        response = self.client.get('/old/')
        self.assertEqual(response.status_code, 200)
    def test_all_page_status_code(self):
        response = self.client.get('/all/')
        self.assertEqual(response.status_code, 200)
    def test_new_page_status_code(self):
        response = self.client.get('/new/')
        self.assertEqual(response.status_code, 200)

    def test_static_images_default_image_page_status_code(self):
        if not using_StaticImageView_instead_of_RedirectView:
            response = self.client.get('/static/images/default_image.png')
            self.assertEqual(response.status_code, 200)
    def test_favicon_page_status_code(self):
        response = self.client.get('/favicon.ico')
        self.assertEqual(response.status_code, 200)

    def test_static_images_favicon_page_status_code(self):
        if not using_StaticImageView_instead_of_RedirectView:
            response = self.client.get('/static/images/favicon.ico')
            self.assertEqual(response.status_code, 200)

