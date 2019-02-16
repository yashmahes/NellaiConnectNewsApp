from django.db import models
import datetime


# class NewsDescription(models.Model):
#     heading = models.CharField(max_length=50, blank=True)
#     nonheading = models.CharField(max_length=5550, blank=True)

#     def __str__(self):
#         return self.heading


# class EventsDescription(models.Model):
#     heading = models.CharField(max_length=50, blank=True)
#     nonheading = models.CharField(max_length=5550, blank=True)

#     def __str__(self):
#         return self.heading


class News(models.Model):
    title = models.CharField(max_length=250, blank=True)
    location = models.CharField(max_length=250, blank=True)
    description = models.TextField(max_length=2550, blank=True)
    # Description = models.ForeignKey(to_field=)
    #Description = models.ManyToManyField(NewsDescription, blank=True)

    category = models.CharField(max_length=50, blank=True)

    image = models.ImageField(blank=True)

    #created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Events(models.Model):
    title = models.CharField(max_length=50, blank=True)
    date = models.CharField(max_length=50, blank=True)
    from_time = models.CharField(max_length=50, blank=True)
    to_time = models.CharField(max_length=50, blank=True)
    location = models.CharField(max_length=150, blank=True)
    # Description = models.ManyToManyField(NewsDescription, blank=True)
    description = models.TextField(max_length=2550, blank=True)

    organiserDetails = models.TextField(max_length=1550, blank=True)
    image = models.ImageField(blank=True)

    #created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


# class StoriesDescription(models.Model):
#     category = models.CharField(max_length=50, blank=True)
#     string = models.CharField(max_length=5550, blank=True)

#     def __str__(self):
#         return self.category


class Stories(models.Model):
    title = models.CharField(max_length=50, blank=True)
    description_heading = models.TextField(max_length=550, blank=True)
    description_nonheading = models.TextField(max_length=1550, blank=True)

    # Description = models.ManyToManyField(StoriesDescription, blank=True)
    image = models.ImageField(blank=True)

    #created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


# class ClassifiedsDescription(models.Model):
#     category = models.CharField(max_length=50, blank=True)
#     string = models.CharField(max_length=5550, blank=True)

#     def __str__(self):
#         return self.category


# class ClassifiedsContact(models.Model):
#     string = models.CharField(max_length=5550, blank=True)

#     def __str__(self):
#         return self.string


class Classifieds(models.Model):
    title = models.CharField(max_length=50, blank=True)
    companyName = models.CharField(max_length=50, blank=True)
    contact = models.TextField(max_length=550, blank=True)
    description = models.TextField(max_length=1550, blank=True)
    #contact = models.ManyToManyField(ClassifiedsContact, blank=True)
    # Description = models.CharField(max_length=550)
    # Description = DescriptionModel(many=True)
    #description = models.ManyToManyField(ClassifiedsDescription, blank=True)
    image = models.ImageField(blank=True)

    #created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


# class JobsOtherDetails(models.Model):
#     detail_string = models.CharField(max_length=5550, blank=True)

#     def __str__(self):
#         return self.detail_string


class Jobs(models.Model):
    title = models.CharField(max_length=50, blank=True)
    company = models.CharField(max_length=50, blank=True)
    experience = models.CharField(max_length=550, blank=True)
    email = models.EmailField()
    otherdetails = models.TextField(max_length=1550, blank=True)
    # Image = models.ImageField()

    #created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


# class Jogging(models.Model):
#     location = models.CharField(max_length=50)
#     date = models.DateField(blank=True, null=True)
#     distance = models.IntegerField()
#     start_time = models.DateTimeField()
#     end_time = models.DateTimeField()
#     weather_condition = models.CharField(max_length=255, blank=True, null=True)
#     user_id = models.IntegerField()

#     def __str__(self):
#         return self.location
