from django.conf.urls import url
from .views import SearchProjects


app_name = 'search'
urlpatterns = [
    url(r'^', SearchProjects.as_view(), name='query'),
]
