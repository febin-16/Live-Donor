from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .serializers import BloodRequestSerializer,BloodDonationSerializer,UserSerializer
from .models import BloodRequest,BloodDonation,User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class UserViewSet(APIView):
     def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status":"success"}, status=status.HTTP_201_CREATED)
        else:
            return Response({"status":"failed"}, status=status.HTTP_400_BAD_REQUEST)

class BloodRequestViewSet(APIView):
    def post(self, request, format=None):
        serializer = BloodRequestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def get(self, request, format=None):
        id=request.query_params.get("id")
        user =BloodRequest.objects.get(id=id)
        serializer = BloodRequestSerializer(user)
        return Response(serializer.data)


    
    
class BloodDonationViewSet(generics.ListCreateAPIView):
    queryset = BloodDonation.objects.all()
    serializer_class = BloodDonationSerializer
    

    