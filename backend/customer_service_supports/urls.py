from django.urls import path

from .views import ListCustomerServiceSupport, DetailCustomerServiceSupport

urlpatterns = [
    path("<int:pk>/", DetailCustomerServiceSupport.as_view()),
    path('', ListCustomerServiceSupport.as_view()),
]
