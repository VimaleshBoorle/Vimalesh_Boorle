# contacts/urls.py

from django.urls import path

from .views import TaskCreateView, TaskListView, WelcomeView

urlpatterns = [
    path("", WelcomeView.as_view(), name="welcome"),  # Add this line for the welcome page
    path("create/", TaskCreateView.as_view(), name="task_create"),
    path("home/", TaskListView.as_view(), name="task_list"),
]

