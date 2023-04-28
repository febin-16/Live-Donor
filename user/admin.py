from django.contrib import admin
from .models import User,BloodDonation,BloodRequest

# Register your models here.
admin.site.register(User)
admin.site.register(BloodDonation)
admin.site.register(BloodRequest)
