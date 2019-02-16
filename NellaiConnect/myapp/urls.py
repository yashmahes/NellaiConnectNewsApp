from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from rest_framework import routers
import os
from . import views

router = routers.DefaultRouter()
router.register('news', views.NewsViewSet)
router.register('events', views.EventsViewSet)
router.register('jobs', views.JobsViewSet)
router.register('classifieds', views.ClassifiedsViewSet)
router.register('stories', views.StoriesViewSet)


urlpatterns = [
    path('', include(router.urls)),

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
