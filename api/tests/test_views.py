from django.test import TestCase, Client
from django.urls import reverse
from api.models import InfoUpload, CvFileUpload

"""Testing views"""
class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.home_url = reverse('home')
        self.info_upload_url = reverse('info-upload')
        self.cv_file_upload_url = reverse('cv-upload')

    # Test login view
    def test_login_view(self):
        response = self.client.post(self.home_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'api/index.html')

    # Test info upload view
    def test_info_upload_view(self):
        response = self.client.post(self.info_upload_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'api/info-upload.html')

    # Test cv upload view
    def test_cv_upload_view(self):
        response = self.client.post(self.cv_file_upload_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'api/cv-upload.html')