from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('gestion_materiel/', include('gestion_materiel.urls')),
]
