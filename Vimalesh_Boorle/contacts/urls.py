# contacts/urls.py

from django.urls import path

from .views import TaskCreateView, TaskDeleteView, TaskDetailView, TaskListView, TaskUpdateView,WelcomeView

urlpatterns = [
    path("", WelcomeView.as_view(), name="welcome"),  # Add this line for the welcome page
    path("contacts/<int:pk>/", TaskDetailView.as_view(), name="task_detail"),
    path("create/", TaskCreateView.as_view(), name="task_create"),
    path("home/", TaskListView.as_view(), name="task_list"),
]

