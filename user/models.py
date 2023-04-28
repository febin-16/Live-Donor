#from django.db import models

# Create your models here.
from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)
    blood_group = models.CharField(max_length=3)
    contact_number = models.CharField(max_length=15)
    location = models.CharField(max_length=200)

    def _str_(self):
        return f"{self.name}"

class BloodRequest(models.Model):
    requester = models.ForeignKey(User, on_delete=models.CASCADE, related_name='requests')
    blood_group = models.CharField(max_length=3)
    quantity = models.IntegerField()
    location = models.CharField(max_length=200)
    contact_number = models.CharField(max_length=15)

    def _str_(self):
        return f"{self.requester.name} ({self.blood_group}): {self.quantity} units in {self.location}"

class BloodDonation(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    )
    requester = models.ForeignKey(BloodRequest, on_delete=models.CASCADE, related_name='requests',default=1)
    blood_group = models.CharField(max_length=3)
    age = models.PositiveIntegerField(default=0)
    weight = models.PositiveIntegerField(default=50)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES,default='M')
    donor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='donations')
    location = models.CharField(max_length=200)
    contact_number = models.CharField(max_length=15)