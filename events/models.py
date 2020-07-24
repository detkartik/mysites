from django.db import models

# Create your models here.


class Event(models.Model):
    name = models.CharField(max_length=150, null=True, blank=True)
    day = models.DateField(u'Day of the event', help_text=u'Day of the event')
    start_time = models.TimeField(u'Starting time', help_text=u'Starting time')
    end_time = models.TimeField(u'Final time', help_text=u'Final time')
    notes = models.TextField(
        u'Textual Notes', help_text=u'Textual Notes', blank=True, null=True)

    def __str__(self):
        return "{}".format(self.name)
