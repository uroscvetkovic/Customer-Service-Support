from django.db import models

class CustomerServiceSupport(models.Model):

    name = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=12, blank=True)
    company = models.CharField(max_length=200, blank=True)
    email = models.EmailField(max_length=200)
    subject = models.CharField(max_length=200)
    problem_desciption = models.TextField()
    date_time_callback = models.DateTimeField(blank=True, null=True)
    submited_at = models.DateTimeField(auto_now_add=True)
    comment = models.TextField(blank=True)
    arhived = models.BooleanField(default=False)

    def __str__(self):
        return self.subject
