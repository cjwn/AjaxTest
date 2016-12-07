from django.conf.urls import url
from main.views import data, update

urlpatterns = [
    url(r'^data/(?P<id>\d+)/$', data),
    url(r'^update/', update)
]
