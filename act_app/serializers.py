from .models import activity,member
from rest_framework import serializers

class member_serialize(serializers.ModelSerializer):
    class Meta:
        model = member
        fields = ['id', 'real_name','timezone']

class activity_serialize(serializers.ModelSerializer):
    class Meta:
        model = member
        fields = ['id', 'start_time','end_time']