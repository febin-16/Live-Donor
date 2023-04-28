from rest_framework import serializers
from .models import User, BloodRequest, BloodDonation

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class BloodRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = BloodRequest
        fields = '__all__'

class BloodDonationSerializer(serializers.ModelSerializer):
    class Meta:
        model = BloodRequest
        fields = '__all__'        