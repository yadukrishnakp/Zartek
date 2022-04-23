from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Story(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    story_name = models.CharField(max_length=100, null=False)
    story_description = models.TextField(null=True, blank=True)
    story_created_date = models.DateField(auto_now_add=True)
    story_image = models.ImageField(upload_to="static/images", null=True, blank=True)

    def __str__(self):
        return str(self.id)


class StoryInformation(models.Model):
    LikeOrDislike = (
        ('like', 'Like'),
        ('dislike', 'Dislike'),
    )
    story_id = models.ForeignKey(Story, on_delete=models.CASCADE)
    user_details = models.ForeignKey(User, on_delete=models.CASCADE)
    story_status = models.CharField(max_length=50, choices=LikeOrDislike)

    def __str__(self):
        return self.story_status


