from django.contrib import admin
from .models import *
from amigos_cafe.models import Booking
# Register your models here.

admin.site.register(Profile)
admin.site.register(Booking)