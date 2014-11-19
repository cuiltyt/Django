from django.contrib import admin
from track.models import Athlete, Event, Record

class RecordsInline(admin.StackedInline):
    model = Record
    extra = 3


class AthletesAdmin(admin.ModelAdmin):
    inlines = [RecordsInline]
    
admin.site.register(Athlete, AthletesAdmin)
admin.site.register(Event)
admin.site.register(Record)