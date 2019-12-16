from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings
from goroskop import views
from .views import *


urlpatterns = [
    path('profiles/<str:slug>/', post_detail, name='post_detail_url'),
    path('', views.compatibility_view),
]
if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()+static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )