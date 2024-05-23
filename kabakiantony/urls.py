from .admin import ka_admin_site

from django.urls import path, include

urlpatterns = [
    path('admin/', ka_admin_site.urls),
    path('', include('me.urls'))
]
