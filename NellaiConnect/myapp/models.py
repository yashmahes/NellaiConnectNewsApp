from django.db import models
import datetime


class NewsDescription(models.Model):
    heading = models.CharField(max_length=50)
    nonheading = models.CharField(max_length=550)


class News(models.Model):
    Title = models.CharField(max_length=50)
    Location = models.CharField(max_length=50)
    #Description = models.CharField(max_length=550)
    # Description = models.ForeignKey(to_field=)
    Description = models.ManyToManyField(NewsDescription, blank=True)

    Category = models.CharField(max_length=50)
    Image = models.ImageField()

    #created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Title


class Events(models.Model):
    Title = models.CharField(max_length=50)
    Event_Date = models.CharField(max_length=50)
    Event_Time = models.CharField(max_length=50)
    Location = models.CharField(max_length=150)
    Description = models.ManyToManyField(NewsDescription, blank=True)
    # Description = models.CharField(max_length=550)
    # Description = DescriptionModel(many=True)
    Organizer_details = models.CharField(max_length=150)
    Image = models.ImageField()

    #created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Title


class Stories(models.Model):
    Title = models.CharField(max_length=50)
    # Description = models.CharField(max_length=550)
    # Description = DescriptionModel(many=True)
    Description = models.ManyToManyField(NewsDescription, blank=True)
    Image = models.ImageField()

    #created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Title


class Classifieds(models.Model):
    Title = models.CharField(max_length=50)
    Company_name = models.CharField(max_length=50)
    Contact_details = models.CharField(max_length=550)
    # Description = models.CharField(max_length=550)
    # Description = DescriptionModel(many=True)
    Description = models.ManyToManyField(NewsDescription, blank=True)
    Image = models.ImageField()

    #created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Title


class Jobs(models.Model):
    Title = models.CharField(max_length=50)
    Company_name = models.CharField(max_length=50)
    Experience = models.CharField(max_length=550)
    Email = models.EmailField()
    Other_details = models.CharField(max_length=550)
    # Image = models.ImageField()

    #created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Title


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
