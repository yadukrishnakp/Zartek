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


# Check likes and dislikes of individual stories
@api_view(['GET'])
def CountLikeDislike(request, pk):
    story = Story.objects.get(id=pk)
    data = story.storyinformation_set.all()
    like_count = data.filter(story_status='like').count()
    dislike_count = data.filter(story_status='dislike').count()
    contexts = {'likes': like_count, 'dislikes': dislike_count}
    return Response(contexts)
