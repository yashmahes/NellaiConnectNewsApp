from rest_framework import serializers
from .models import News, Events, Stories, Classifieds, Jobs


class NewsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = News
        fields = ("id", 'title', 'location', 'description',
                  'category', 'image')


class EventsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Events
        fields = ("id", 'title', 'location', 'description',
                  'date', 'from_time', 'to_time', 'organiserDetails', 'image')


class StoriesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Stories
        fields = ("id", 'title', 'description_heading',
                  'description_nonheading', 'image')


class ClassifiedsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Classifieds
        fields = ("id", 'title', 'companyName',
                  'contact', 'description_heading',
                  'description_nonheading', 'image')


class JobsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Jobs
        fields = ("id", 'title', 'company', 'experience',
                  'email', 'otherdetails')
