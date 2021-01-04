from django.contrib import admin
from prjWebApp.models import Topic, Entry


# Register your models here
class TopicAdmin(admin.ModelAdmin):
    pass


admin.site.register(Topic, TopicAdmin)
admin.site.register(Entry, TopicAdmin)