from django.test import TestCase

from .models import CustomerServiceSupport

class CustomerServiceSupportModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        CustomerServiceSupport.objects.create(
            name = 'somename',
            phone_number = '123456789',
            company = 'somecompany',
            email = 'somemail@mail.com',
            subject = 'somesubject',
            problem_desciption = 'someproblemdesciption',
            comment = 'somecomment'
        )

    def test_subject_content(self):
        csSupport = CustomerServiceSupport.objects.get(id=1)
        expected_subject = f'{csSupport.subject}'
        self.assertEquals(expected_subject, 'somesubject')

            
        
