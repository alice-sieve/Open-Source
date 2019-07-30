from django.shortcuts import render
from .models import Projects
from django.views.generic import ListView

class ProjectsList(ListView):
    template_name = 'projects/list.html'

    def get_content_data(self, *args, **kwargs):
        context = super(ProjectsList, self).get_context_data(*args, **kwargs)
        return context
    
    def get_queryset(self, *args, **kwargs):
        request = self.request
        qs = Projects.objects.all()
        return qs
