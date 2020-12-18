from django.test import SimpleTestCase
from django.urls import reverse, resolve
from api.views import login_view, info_upload_view, cv_file_upload_view

"""Testing urls"""
class TestUrls(SimpleTestCase):

    # Test home url
    def test_home_url_is_resolved(self):
        url = reverse('home')
        self.assertEquals(resolve(url).func, login_view)

    # Test info-upload url
    def test_info_upload_url_is_resolved(self):
        url = reverse('info-upload')
        self.assertEquals(resolve(url).func, info_upload_view)

    # Test cv-upload url
    def test_cv_upload_url_is_resolved(self):
        url = reverse('cv-upload')
        self.assertEquals(resolve(url).func, cv_file_upload_view)
