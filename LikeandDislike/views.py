from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Story, StoryInformation
from .serializers import StorySerializer, StoryInformationSerializer


# show all stories added by admin
@api_view(['GET'])
def ShowAllStories(request):
    stories = Story.objects.all()
    serializer = StorySerializer(stories, many=True)
    return Response(serializer.data)


# show story added by admin
@api_view(['GET'])
def ShowStory(request, pk):
    story = Story.objects.get(id=pk)
    serializer = StorySerializer(story)
    return Response(serializer.data)
