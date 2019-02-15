from django.contrib import admin

# Register your models here.
from .models import Jobs, Classifieds, Stories, Events, News
admin.site.register(News)
admin.site.register(Events)
admin.site.register(Stories)
admin.site.register(Classifieds)
admin.site.register(Jobs)
