from django.urls import path

from .views import home, projects, blogs

app_name = "me"

urlpatterns = [
    path('', home, name="home"),
    path('projects/', projects, name="projects"),
    path('articles/', blogs, name="articles"),
]
