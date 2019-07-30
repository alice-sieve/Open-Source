import random
import string
from django.utils.text import slugify

# Generating random string
def random_string_generator(size=10, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

# Unique slug generator
def unique_slug_generator(instance, new_slug=None):
    if new_slug is not None:
        slug = new_slug
    else:
        slug = slugify(instance.title)

    instance_class = instance.__class__
    qs = instance_class.objects.filter(slug=slug).exists()
    if qs:
        new_slug = "{slug}-{randStr}".format(slug=slug, randStr=unique_slug_generator(size=4))
        return  unique_slug_generator(instance, new_slug=new_slug)
    return slug
