from rest_framework import serializers
from .models import News, Events, Stories, Classifieds, Jobs


class NewsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = News
        fields = ("id", 'Title', 'Location', 'Description',
                  'Category', 'Image')


class EventsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Events
        fields = ("id", 'Title', 'Location', 'Description',
                  'Event_Date', 'Event_Time', 'Organizer_details', 'Image')


class StoriesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Stories
        fields = ("id", 'Title', 'Description', 'Image')


class ClassifiedsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Classifieds
        fields = ("id", 'Title', 'Description', 'Image',
                  'Company_name', 'Contact_details')


class JobsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Jobs
        fields = ("id", 'Title', 'Email', 'Experience',
                  'Company_name', 'Other_details')
