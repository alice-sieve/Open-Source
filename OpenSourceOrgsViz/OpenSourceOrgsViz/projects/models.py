import os
import random
from django.db import models
from django.db.models import Q
from .utils import unique_slug_generator
from django.db.models.signals import pre_save


# Function for spiliting the filename
def get_image_name(filename):
    basename = os.path.basename(filename)
    filename, ext = os.path.splitext(basename)
    return filename, ext


# Function returning the storing address of image
def image_upload(instance, filename):
    filename, ext = get_image_name(filename)
    randNum = random.randint(1, 1000000)
    newFileName = "{randNum}{filename}{ext}".format(
        randNum=randNum,
        filename=filename,
        ext=ext
    )
    return "products/{newFileName}".format(newFileName=newFileName)


# Custom queryset
class ProjectsQuerySet(models.query.QuerySet):

    def search(self, query):
        lookups = Q(title__icontains=query) | \
            Q(description__icontains=query)

        return self.filter(lookups).distinct()


# Custom model manager
class ProjectsManager(models.Manager):

    def get_queryset(self):
        return ProjectsQuerySet(self.model, using=self._db)

    def search(self, query):
        return self.get_queryset().search(query)


# Model class for projects
class Projects(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField(unique=True, blank=True)
    description = models.TextField()
    image = models.ImageField(upload_to=image_upload, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    objects = ProjectsManager()

    def __str__(self):
        return self.title


# Fetching slug if it not exists from utils.py
def pre_save_slug_generator(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


# pre saving slug before the models get saved
pre_save.connect(pre_save_slug_generator, sender=Projects)
