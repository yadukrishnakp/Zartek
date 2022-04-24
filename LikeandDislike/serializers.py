from rest_framework import serializers
from .models import Story, StoryInformation

from django.contrib.auth.models import User


class StorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Story
        fields = '__all__'


class StoryInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = StoryInformation
        fields = '__all__'
