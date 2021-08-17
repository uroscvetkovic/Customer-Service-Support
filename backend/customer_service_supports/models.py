from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
import datetime 

def validateDateTime(value):
    day = value.weekday()
    hour = value.hour
    if day == 6:
        raise ValidationError(
            _('%(value)s date day is sunday'),
            params={'value': value},
        )
    elif day == 5 and not (8 <= hour <= 13):
        raise ValidationError(
            _('Saturday time is not in time limit'),
            params={'value': value},
        )
    elif not (8 <= hour <= 20):
        raise ValidationError(
            _('Time is not in time limit'),
            params={'value': value},
        )



class CustomerServiceSupport(models.Model):

    name = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=12, blank=True)
    company = models.CharField(max_length=200, blank=True)
    email = models.EmailField(max_length=200)
    subject = models.CharField(max_length=200)
    problem_desciption = models.TextField()
    date_time_callback = models.DateTimeField(blank=True, null=True, validators=[validateDateTime])
    submited_at = models.DateTimeField(auto_now_add=True)
    comment = models.TextField(blank=True)
    archived = models.BooleanField(default=False)

    def __str__(self):
        return self.subject
