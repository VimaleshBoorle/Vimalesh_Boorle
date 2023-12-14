# contacts/urls.py

from django.urls import path

from .views import TaskListView, WelcomeView

urlpatterns = [
    path("", WelcomeView.as_view(), name="welcome"),  # Add this line for the welcome page
    path("home/", TaskListView.as_view(), name="task_list"),
]

