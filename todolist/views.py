from django.contrib.auth.decorators import login_required
# Create your views here.
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

from .forms import TaskForm
from .models import Task, Tags


@login_required
def home(request):
    context = {}
    return render(request, 'home.html', context)


class ListTasksView(LoginRequiredMixin, ListView):
    model = Task
    template_name = 'task_list.html'
    context_object_name = 'tasks'

    def get_queryset(self, *args, **kwargs):
        query = super(ListTasksView, self).get_queryset(*args, **kwargs)
        print(self.request.user)
        return query.filter(user=self.request.user)


class CreateTaskView(LoginRequiredMixin, CreateView):
    template_name = 'task_create.html'
    form_class = TaskForm
    success_url = reverse_lazy('tasks:home')

    def get_context_data(self, **kwargs):
        context = super(CreateTaskView, self).get_context_data(**kwargs)
        context['tags'] = Tags.objects.all()
        context['user'] = self.request.user
        return context
