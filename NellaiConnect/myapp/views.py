from django.shortcuts import render
from rest_framework import viewsets
from .serializers import NewsSerializer, StoriesSerializer, EventsSerializer, JobsSerializer, ClassifiedsSerializer
from .models import News, Events, Stories, Classifieds, Jobs
from rest_framework.decorators import api_view
from rest_framework.response import Response


class NewsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows News to be viewed or edited.
    """
    queryset = News.objects.all()
    serializer_class = NewsSerializer


@api_view(['GET'])
def getNews(request, id=0):
    if id == 0:
        data = []
        db_data = News.objects.all()
        for db_obj in db_data:
            required_data_obj = {}
            required_data_obj['id'] = db_obj.id
            required_data_obj['title'] = db_obj.title
            required_data_obj['location'] = db_obj.location
            required_data_obj['category'] = db_obj.category
            required_data_obj['description'] = db_obj.description.split("\r\n")
            #required_data_obj['image'] = db_obj.image
            data.append(required_data_obj)

        return Response({"News": data})

    else:
        db_data = News.objects.filter(id=id)
        required_data_obj = {}
        for db_obj in db_data:
            required_data_obj['id'] = db_obj.id
            required_data_obj['title'] = db_obj.title
            required_data_obj['location'] = db_obj.location
            required_data_obj['category'] = db_obj.category
            required_data_obj['description'] = db_obj.description.split("\r\n")
            # required_data_obj['image'] = db_obj.image
            break
        return Response({"News": required_data_obj})


@api_view(['GET'])
def getNewsByCategory(request, category=""):

    data = []
    db_data = News.objects.filter(category=category)
    for db_obj in db_data:
        required_data_obj = {}
        required_data_obj['id'] = db_obj.id
        required_data_obj['title'] = db_obj.title
        required_data_obj['location'] = db_obj.location
        required_data_obj['category'] = db_obj.category
        required_data_obj['description'] = db_obj.description.split("\r\n")
        #required_data_obj['image'] = db_obj.image
        print(type(db_obj.image))
        data.append(required_data_obj)

    return Response({"News": data})


class StoriesViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Stories to be viewed or edited.
    """
    queryset = Stories.objects.all()
    serializer_class = StoriesSerializer


@api_view(['GET'])
def getStories(request, id=0):
    if id == 0:
        data = []
        db_data = Stories.objects.all()
        for db_obj in db_data:
            required_data_obj = {}
            required_data_obj['id'] = db_obj.id
            required_data_obj['title'] = db_obj.title
            required_data_obj['description'] = []

            description_heading = db_obj.description_heading.split("\r\n")
            description_nonheading = db_obj.description_nonheading.split(
                "\r\n")

            for desc in description_heading:
                required_data_obj['description'].append({"heading": desc})

            for desc in description_nonheading:
                required_data_obj['description'].append({"nonheading": desc})

            #required_data_obj['image'] = db_obj.image
            data.append(required_data_obj)

        return Response({"Stories": data})

    else:
        db_data = Stories.objects.filter(id=id)
        required_data_obj = {}
        for db_obj in db_data:
            required_data_obj['id'] = db_obj.id
            required_data_obj['title'] = db_obj.title

            required_data_obj['description'] = []

            description_heading = db_obj.description_heading.split("\r\n")
            description_nonheading = db_obj.description_nonheading.split(
                "\r\n")

            for desc in description_heading:
                required_data_obj['description'].append({"heading": desc})

            for desc in description_nonheading:
                required_data_obj['description'].append({"nonheading": desc})
            #required_data_obj['image'] = db_obj.image
            break

        return Response({"Stories": required_data_obj})


class EventsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Events to be viewed or edited.
    """
    queryset = Events.objects.all()
    serializer_class = EventsSerializer


@api_view(['GET'])
def getEvents(request, id=0):
    if id == 0:
        data = []
        db_data = Events.objects.all()
        for db_obj in db_data:
            required_data_obj = {}
            required_data_obj['id'] = db_obj.id
            required_data_obj['title'] = db_obj.title
            required_data_obj['date'] = db_obj.date
            required_data_obj['from_time'] = db_obj.from_time
            required_data_obj['to_time'] = db_obj.to_time
            required_data_obj['location'] = db_obj.location

            required_data_obj['description'] = db_obj.description.split("\r\n")
            required_data_obj['organiserDetails'] = db_obj.organiserDetails.split(
                "\r\n")
            #required_data_obj['image'] = db_obj.image
            data.append(required_data_obj)

        return Response({"Events": data})

    else:
        db_data = Events.objects.filter(id=id)
        required_data_obj = {}
        for db_obj in db_data:
            required_data_obj['id'] = db_obj.id
            required_data_obj['title'] = db_obj.title
            required_data_obj['date'] = db_obj.date
            required_data_obj['from_time'] = db_obj.from_time
            required_data_obj['to_time'] = db_obj.to_time
            required_data_obj['location'] = db_obj.location

            required_data_obj['description'] = db_obj.description.split("\r\n")
            required_data_obj['organiserDetails'] = db_obj.organiserDetails.split(
                "\r\n")
            # required_data_obj['image'] = db_obj.image
            break

        return Response({"Events": required_data_obj})


class ClassifiedsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Classifieds to be viewed or edited.
    """
    queryset = Classifieds.objects.all()
    serializer_class = ClassifiedsSerializer


@api_view(['GET'])
def getClassifieds(request, id=0):
    if id == 0:
        data = []
        db_data = Classifieds.objects.all()
        for db_obj in db_data:
            required_data_obj = {}
            required_data_obj['id'] = db_obj.id
            required_data_obj['title'] = db_obj.title
            required_data_obj['companyName'] = db_obj.companyName
            required_data_obj['description'] = []

            description_heading = db_obj.description_heading.split("\r\n")
            description_nonheading = db_obj.description_nonheading.split(
                "\r\n")

            for desc in description_heading:
                required_data_obj['description'].append({"heading": desc})

            for desc in description_nonheading:
                required_data_obj['description'].append({"nonheading": desc})

            required_data_obj['contact'] = db_obj.contact.split("\r\n")
            #required_data_obj['image'] = db_obj.image
            data.append(required_data_obj)

        return Response({"Classifieds": data})

    else:
        db_data = Classifieds.objects.filter(id=id)
        required_data_obj = {}
        for db_obj in db_data:
            required_data_obj['id'] = db_obj.id
            required_data_obj['title'] = db_obj.title
            required_data_obj['companyName'] = db_obj.companyName
            required_data_obj['description'] = []

            description_heading = db_obj.description_heading.split("\r\n")
            description_nonheading = db_obj.description_nonheading.split(
                "\r\n")

            for desc in description_heading:
                required_data_obj['description'].append({"heading": desc})

            for desc in description_nonheading:
                required_data_obj['description'].append({"nonheading": desc})

            required_data_obj['contact'] = db_obj.contact.split("\r\n")
            #required_data_obj['image'] = db_obj.image
            break

        return Response({"Classifieds": required_data_obj})


class JobsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Jobs to be viewed or edited.
    """
    queryset = Jobs.objects.all()
    serializer_class = JobsSerializer


@api_view(['GET'])
def getJobs(request, id=0):
    if id == 0:
        data = []
        db_data = Jobs.objects.all()
        for db_obj in db_data:
            required_data_obj = {}
            required_data_obj['id'] = db_obj.id
            required_data_obj['title'] = db_obj.title
            required_data_obj['company'] = db_obj.company
            required_data_obj['experience'] = db_obj.experience
            required_data_obj['email'] = db_obj.email
            required_data_obj['otherdetails'] = db_obj.otherdetails.split(
                "\r\n")

            #required_data_obj['image'] = db_obj.image
            data.append(required_data_obj)

        return Response({"Jobs": data})

    else:
        db_data = Jobs.objects.filter(id=id)
        required_data_obj = {}
        for db_obj in db_data:
            required_data_obj['id'] = db_obj.id
            required_data_obj['title'] = db_obj.title
            required_data_obj['company'] = db_obj.company
            required_data_obj['experience'] = db_obj.experience
            required_data_obj['email'] = db_obj.email
            required_data_obj['otherdetails'] = db_obj.otherdetails.split(
                "\r\n")
            # required_data_obj['image'] = db_obj.image
            break

        return Response({"Jobs": required_data_obj})
