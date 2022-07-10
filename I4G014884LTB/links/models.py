from django.db import models
from django.contrib.auth import get_user_model
from django.template.defaultfilters import slugify


# Create your models here.
class Link(models.Model):
    target_url = models.URLField(max_length=200)
    description = models.CharField(max_length=200)
    identifier = models.SlugField(max_length=20, blank=True, unique=True)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)


    def save(self, *args, **kwargs):
        self.slug = slugify(self.identifier)
        super(Link, self).save(*args, **kwargs)
        pass 

    def __str__(self):
        return f"Short Url for: {self.target_url} is {self.identifier}"
