from django.contrib import admin

# Register your models here.
from . import models

admin.site.register(models.Event)
admin.site.register(models.Visitor)