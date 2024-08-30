from django.contrib import admin
from django.urls import path, include
from mailings.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),  # Связываем корневой URL с представлением home
    path('mailings/', include('mailings.urls')),
]
