from django.urls import path
from . import views

urlpatterns = [
    path('show_all_stories/', views.ShowAllStory.as_view(), name="show_all_stories"),
    path('show_story/<str:pk>/', views.ShowStory.as_view(), name="show_story"),
    path('like_dislike_count/<str:pk>/', views.CountLikeDislike.as_view(), name="like_dislike_count"),
    path('user_liked_story/<str:pk>/', views.UserLikedStory.as_view(), name="user_liked_story"),
    path('user_disliked_story/<str:pk>/', views.UserDislikedStory.as_view(), name="user_disliked_story")
]
