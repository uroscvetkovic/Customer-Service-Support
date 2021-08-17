from django.test import TestCase
from django.test import Client
from django.urls import reverse

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
            date_time_callback = '2021-08-20 11:30:00+00:00',
            problem_desciption = 'someproblemdesciption',
            comment = 'somecomment'
        )

    def test_subject_content(self):
        csSupport = CustomerServiceSupport.objects.get(id=1)
        expected_subject = f'{csSupport.subject}'
        self.assertEquals(expected_subject, 'somesubject')

    def test_phone_number_content(self):
        csSupport = CustomerServiceSupport.objects.get(id=1)
        expected_subject = f'{csSupport.phone_number}'
        self.assertEquals(expected_subject, '123456789')

    def test_date_time_content(self):
        csSupport = CustomerServiceSupport.objects.get(id=1)
        expected_subject = f'{csSupport.date_time_callback}'
        self.assertEquals(expected_subject, '2021-08-20 11:30:00+00:00')

    def test_post_request(self):
        c = Client()
        data = {
             'name' : 'postsomename',
             'phone_number' : '123456789',
             'company' : 'somecompany',
             'email' : 'somemail@mail.com',
             'subject' : 'somesubject',
             'date_time_callback' : '2021-08-20 10:30:00+00:00',
             'problem_desciption' : 'someproblemdesciption',
        }
        response = c.post('/api/', data)
        print("----------->", response)
        self.assertNotContains(response, 'something went wrong', 201)

    
    def test_post_request_time_validation(self):
        c = Client()
        data = {
             'name' : 'postsomename',
             'phone_number' : '123456789',
             'company' : 'somecompany',
             'email' : 'somemail@mail.com',
             'subject' : 'somesubject',
             'date_time_callback' : '2021-08-20 23:30:00+00:00',   #bad time 
             'problem_desciption' : 'someproblemdesciption',
        }
        response = c.post('/api/', data)
        print("-----------ssssssssssssssssssss>", response)
        self.assertEquals(response.status_code, 400)


