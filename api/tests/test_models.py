from django.test import TestCase
from api.models import InfoUpload, CvFileUpload, ApiToken, CvFileToken
from django.core.files import File
import uuid
import mock

"""Testing models"""
class TestModels(TestCase):
    def setUp(self):
        
        InfoUpload.objects.create(
            name = 'Mahmudul Sajib',
            email = 'shout.mahmud@gmail.com',
            phone = '+8801994373945',
            full_address = 'Block: A, House: 19, Haque Residential Society Kadamtala, Basabo, Dhaka-1214',
            name_of_university = 'IUBAT',
            graduation_year = 2020,
            cgpa = 3.67,
            experience_in_months = 6,
            current_work_place_name = 'Upwork Inc. (Freelance)',
            applying_in = 'Backend',
            expected_salary = 25000,
            field_buzz_reference = 'Mohammad Ashraful Islam',
            github_project_url = 'https://github.com/mahmud-sajib/FBuzz-Task'
        )
    
    # Test maximum length for phone field of InfoUpload Model
    def test_phone_max_length(self):
        info = InfoUpload.objects.latest('on_spot_creation_time')
        max_length = info._meta.get_field('phone').max_length
        self.assertEqual(max_length, 14)
    
    # Test maximum length for email field of InfoUpload Model
    def test_email_max_length(self):
        info = InfoUpload.objects.latest('on_spot_creation_time')
        max_length = info._meta.get_field('email').max_length
        self.assertEqual(max_length, 256)

    # Test CvFileUpload Model
    def test_file_field(self):
        file_mock = mock.MagicMock(spec=File)
        file_mock.name = 'cv.pdf'
        file_model = CvFileUpload(document=file_mock)
        self.assertEqual(file_model.document.name, file_mock.name)
