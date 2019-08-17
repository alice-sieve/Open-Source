from django.contrib import admin
from .models import Projects

class ProjectsAdmin(admin.ModelAdmin):

    list_display = ['__str__', 'slug']

    class Meta:
        model = Projects

admin.site.register(Projects, ProjectsAdmin)
