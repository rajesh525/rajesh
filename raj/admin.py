from django.contrib import admin

# Register your models here.
from . models import friends,book
admin.site.register(friends)
admin.site.register(book)