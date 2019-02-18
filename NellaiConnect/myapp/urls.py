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
    path('getnews', views.getNews),
    path('getnews/<int:id>', views.getNews),
    path('getnews/<category>', views.getNewsByCategory),

    path('getstories', views.getStories),
    path('getstories/<int:id>', views.getStories),
    path('getevents', views.getEvents),
    path('getevents/<int:id>', views.getEvents),
    path('getclassifieds', views.getClassifieds),
    path('getclassifieds/<int:id>', views.getClassifieds),
    path('getjobs', views.getJobs),
    path('getjobs/<int:id>', views.getJobs),

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
