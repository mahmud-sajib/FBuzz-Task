from django.test import SimpleTestCase
from api.forms import InfoUploadForm, CvFileUploadForm

"""Testing forms"""
class TestForms(SimpleTestCase):

    # Test if InfoUploadForm contains no data
    def test_info_upload_form_invalid_data(self):
        form = InfoUploadForm(data={})
        self.assertFalse(form.is_valid())

    # Test if CvFileUploadForm contains no data
    def test_cv_upload_form_invalid_data(self):
        form = CvFileUploadForm(data={})
        self.assertFalse(form.is_valid())

