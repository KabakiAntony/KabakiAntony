from django.contrib import admin
from kabakiantony.admin import ka_admin_site
from .models import Me, Projects, Blogs


@admin.register(Me, site=ka_admin_site)
class MeAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', "thumb", "url"]
    list_display_links = ['title']
    list_filter = ['title']
    

@admin.register(Projects, site=ka_admin_site)
class ProjectsAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', "thumb", "url"]
    list_display_links = ['title']
    list_filter = ['title']


@admin.register(Blogs, site=ka_admin_site)
class BlogsAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', "thumb", "url"]
    list_display_links = ['title']
    list_filter = ['title']


