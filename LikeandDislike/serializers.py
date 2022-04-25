from rest_framework import serializers
from .models import Story, StoryInformation


class StorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Story
        fields = '__all__'


class StoryInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = StoryInformation
        fields = ('user_id',)
