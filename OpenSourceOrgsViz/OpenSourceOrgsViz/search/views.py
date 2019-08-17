from django.shortcuts import render, redirect
from projects.models import Projects
from django.views.generic import ListView

class SearchProjects(ListView):
    template_name = 'search/list.html'

    def get_context_data(self, *args, **kwargs):
        context = super(SearchProjects, self).get_context_data(*args, **kwargs)
        request = self.request
        query = self.request.GET.get('q')
        context['query'] = query
        return context

    def get_queryset(self):
        request = self.request
        query = request.GET.get('q')
        if query is not None:
            return Projects.objects.search(query)
        else:
            return redirect('/projects')
