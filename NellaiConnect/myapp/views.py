from django.shortcuts import render
from rest_framework import viewsets
from .serializers import NewsSerializer, StoriesSerializer, EventsSerializer, JobsSerializer, ClassifiedsSerializer
from .models import News, Events, Stories, Classifieds, Jobs


class NewsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows News to be viewed or edited.
    """
    queryset = News.objects.all().order_by('-date_joined')
    serializer_class = NewsSerializer


class StoriesViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Stories to be viewed or edited.
    """
    queryset = Stories.objects.all()
    serializer_class = StoriesSerializer


class EventsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Events to be viewed or edited.
    """
    queryset = Events.objects.all().order_by('-date_joined')
    serializer_class = EventsSerializer


class ClassifiedsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Classifieds to be viewed or edited.
    """
    queryset = Classifieds.objects.all()
    serializer_class = ClassifiedsSerializer


class JobsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Jobs to be viewed or edited.
    """
    queryset = Jobs.objects.all()
    serializer_class = JobsSerializer
