from rest_framework import serializers
from .models import User, BloodRequest, BloodDonation
from rest_framework.exceptions import ValidationError
from datetime import timezone
import datetime

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class BloodRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = BloodRequest
        depth = 2
        fields = '__all__'

class BloodDonationSerializer(serializers.ModelSerializer):
    class Meta:
        model = BloodDonation
        depth = 2
        fields = '__all__'     
