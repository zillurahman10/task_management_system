from django.shortcuts import render
from task.models import Task
# Create your views here.
def show_task(request):
    data = Task.objects.all()
    return render(request, 'show_task.html', {'data': data})