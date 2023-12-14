from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView
from django.urls import reverse_lazy
from .models import Task
from .task_form import TaskForm

from django.views.generic import TemplateView

    

class TaskListView(ListView):
    model = Task




class WelcomeView(TemplateView):
    template_name = "welcome.html"
