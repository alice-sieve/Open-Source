from django.conf.urls import url
from .views import ProjectsList

app_name = 'projects'

urlpatterns = [
    url(r'^$', ProjectsList.as_view(), name='home'),
]
