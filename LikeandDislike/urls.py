from django.urls import path
from . import views

urlpatterns = [
    path('show_all_stories/', views.ShowAllStory.as_view(), name="show_all_stories"),
    path('show_story/<str:pk>/', views.ShowStory.as_view(), name="show_story"),
    path('like_and_dislike/<str:pk>/', views.CountLikeDislike.as_view(), name="like_and_dislike")
]
