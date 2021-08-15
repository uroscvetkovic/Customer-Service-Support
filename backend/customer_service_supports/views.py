from rest_framework import generics

from .models import CustomerServiceSupport
from .serializers import CustomerServiceSupportSerializer

class ListCustomerServiceSupport(generics.ListCreateAPIView):
    queryset = CustomerServiceSupport.objects.all()
    serializer_class = CustomerServiceSupportSerializer

class DetailCustomerServiceSupport(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomerServiceSupport.objects.all()
    serializer_class = CustomerServiceSupportSerializer