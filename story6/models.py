from django.db import models

# Create your models here.
class Event(models.Model):
    event = models.CharField(max_length = 50, null = True)
    brief_description = models.CharField(max_length = 200, null = True)
    complete_description = models.TextField(max_length = 2000, null = True)

    def __str__(self):
        return '{}'.format(self.event)

class Visitor(models.Model):
    visitor_name = models.CharField(max_length = 75, null = True)
    visitor_age = models.PositiveIntegerField(null = True)
    ID_TYPE = (
        ('KTM', 'KTM'),
        ('KTP', 'KTP'),
        ('SIM', 'SIM'),
        ('Passport', 'Passport'),
    )
    id_type = models.CharField(
        max_length = 10 ,
        choices = ID_TYPE,
        default = 'KTM',
        null = True
    )
    identity_number = models.CharField(max_length = 75, null = True)
    event = models.ForeignKey(Event, on_delete = models.CASCADE)

    def __str__(self):
        return '{}'.format(self.visitor_name)