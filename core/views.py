from django.shortcuts import render

from todo.models import Project, Todos


# Create your views here.
def index(request):
    todos = Todos.objects.filter(done=False)
    projects = Project.objects.all()

    return render(request, "core/index.html", {"projects": projects, "todos": todos})


def contact(request):
    return render(request, "core/contact.html")
