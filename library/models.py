from django.db import models
from django.utils.text import slugify

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    description = models.TextField()
    published_date = models.DateField()
    slug = models.SlugField(unique=True, blank=True, null=True)


    #slugu avtomatik yaratmagcun
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title) 
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title