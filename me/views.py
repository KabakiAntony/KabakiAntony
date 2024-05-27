from django.shortcuts import render

from .models import Me, Projects, Blogs

def home(request):
    me = Me.objects.first()
    context = {
        "me":me,
    }
    return render(request, "me/index.html", context)


def projects(request):
    projects = Projects.objects.all()
    context = {
        "projects": projects,
    }
    return render(request, "me/projects.html", context)


def blogs(request):
    articles = Blogs.objects.all()
    context = {
        "articles": articles,
    }
    return render(request, "me/blogs.html", context)
