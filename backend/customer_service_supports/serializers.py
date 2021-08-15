from django.db import models
from rest_framework import serializers

from .models import CustomerServiceSupport


class CustomerServiceSupportSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerServiceSupport
        fields = (
            'id', 'name', 'phone_number', 'company', 'email', 
            'subject', 'problem_desciption', 'date_time_callback',
         )