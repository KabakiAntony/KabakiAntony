from django.shortcuts import render


def home(request):
    return render(request, "me/index.html")


def projects(request):
    return render(request, "me/projects.html")


def blogs(request):
    return render(request, "me/blogs.html")
