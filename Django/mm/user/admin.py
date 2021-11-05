from django.contrib import admin

from user.serializers import *
from user.urls import *
from user.signals import *
from user.apps import *
from user.models import profile

admin.site.register(profile)
