from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import home

from goroskop.views import login_view, register_view, logout_view, compatibility_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('goroskop/login/', login_view),
    path('goroskop/register/', register_view),
    path('goroskop/logout/', logout_view),
    path('goroskop/', include("goroskop.urls")),
    path('', compatibility_view),
    path('', include("goroskop.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)