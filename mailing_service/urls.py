from django.urls import path, include
from django.views.generic import RedirectView
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('mailings/', include('mailings.urls')),
    path('', RedirectView.as_view(url='/mailings/', permanent=False)),
]
