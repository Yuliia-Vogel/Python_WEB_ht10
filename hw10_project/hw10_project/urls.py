from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("quotes/", include("quotes.urls")),
    path('users/', include('users.urls')),
]
