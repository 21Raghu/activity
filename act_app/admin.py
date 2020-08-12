from django.contrib import admin
from .models import activity,member
l = [activity,member]
admin.site.register(l)
# Register your models here.
