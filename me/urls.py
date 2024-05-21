from django.urls import path

from .views import home, projects, blogs

urlpatterns = [
    path('', home, name="me"),
    path('projects/', projects, name="projects"),
    path('blogs/', blogs, name="blogs"),
]
