from django.conf.urls import url
from . import views
urlpatterns=[url(r'^$',views.index,name='index'),url(r'^rj/',views.raj,name='raj')
,url(r'artical/(?P<year>[0-9]{4}-[0-9]{2}-[0-9]{2})/',views.year_arch),url(r'raj/(?P<rol>[a-zA-Z0-9]{10})/',views.stud,name="raj")
,url(r'submit/',views.intd,name='sub'),
url(r'rep/',views.std,name='form'),url(r'art/',views.art,name='art'),url(r'ar/',views.ar,name='a'),url(r'alt/',views.gt,name='getart'),url(r'prof/',views.pro,name='profit')]
