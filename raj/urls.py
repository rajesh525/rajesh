from django.conf.urls import url
from . import views
from django.contrib import admin
admin.site.site_header='administration of raj & polls apps'
admin.site.site_title='polls&raj'
admin.site.site_index='hello '
urlpatterns=[
url(r's/',views.raj,name='roc'),url(r'form/',views.nmform,name='fm'),
url(r'sub/',views.nm,name='nm'),
url(r'media/books/(?P<img>[0-9a-zA-Z._]+[.][a-zA-Z]{2,4})/',views.img,name='mg')
]