from django.urls import path
from . import views

urlpatterns = {
    path('show_all_stories/', views.ShowAllStories, name="show_all_stories"),
    path('show_story/<str:pk>', views.ShowStory, name="show_story"),
    path('like_and_dislike/<str:pk>', views.CountLikeDislike, name="like_and_dislike")
}