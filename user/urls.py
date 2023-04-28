from django.urls import path
from .views import BloodRequestViewSet,BloodDonationViewSet,UserViewSet

urlpatterns = [
    path('user/', UserViewSet.as_view(), name='donation-list'),
    path('bloodrequest/', BloodRequestViewSet.as_view(), name='request-list'),
    path('blooddonation/', BloodDonationViewSet.as_view(), name='donation-list'),
]