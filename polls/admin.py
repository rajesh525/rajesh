from django.contrib import admin
from .models import Reporter
from .models import raj,choice,profit
# Register your models here
from .import models
admin.site.register(models.Artical)
admin.site.register(models.Reporter)
admin.site.register(models.raj)
admin.site.register(models.choice)
admin.site.register(models.profit)