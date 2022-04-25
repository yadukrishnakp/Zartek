from rest_framework.response import Response

from .models import Story, StoryInformation
from .serializers import StorySerializer, StoryInformationSerializer

from rest_framework.views import APIView


# show all stories added by admin.
class ShowAllStory(APIView):
    def get(self, request):
        stories = Story.objects.all()
        serializer = StorySerializer(stories, many=True)
        return Response(serializer.data)


# show story added by admin.
class ShowStory(APIView):
    def get(self, request, pk):
        story = Story.objects.get(id=pk)
        serializer = StorySerializer(story)
        return Response(serializer.data)


# Check likes and dislikes of individual stories.
class CountLikeDislike(APIView):
    def get(self, request, pk):
        story = Story.objects.get(id=pk)
        data = story.storyinformation_set.all()
        like_count = data.filter(story_status='like').count()
        dislike_count = data.filter(story_status='dislike').count()
        contexts = {'likes': like_count, 'dislikes': dislike_count}
        return Response(contexts)


# check a story liked users.
class UserLikedStory(APIView):
    def get(self, request, pk):
        filter_stories = StoryInformation.objects.filter(story_status='like', story_id=pk)
        serialized_stories = StoryInformationSerializer(filter_stories, many=True)
        return Response(serialized_stories.data)


# check a story disliked users.
class UserDislikedStory(APIView):
    def get(self, request, pk):
        filter_stories = StoryInformation.objects.filter(story_status='dislike', story_id=pk)
        serialized_stories = StoryInformationSerializer(filter_stories, many=True)
        return Response(serialized_stories.data)
