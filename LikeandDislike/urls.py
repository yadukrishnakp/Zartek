from django.urls import path
from . import views

urlpatterns = [
    path('create_story/', views.CreateStory, name="create_story")
]