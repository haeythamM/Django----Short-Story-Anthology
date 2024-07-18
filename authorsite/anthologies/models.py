from django.db import models
from authors.models import Author

class Collection(models.Model):
    title = models.CharField(max_length=255)
    authors = models.ManyToManyField(Author, blank=True, related_name='anthologiesf')
    def __str__(self):
        return self.title[:50]

class Cover(models.Model):
    collection = models.OneToOneField(Collection, on_delete=models.CASCADE, primary_key=True, related_name='cover')
    image = models.ImageField(upload_to='anthologies/covers/%Y/%m/%d/')
    def __str__(self):
        return self.image[:50]

class Story(models.Model):
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE, related_name='stories')
    title = models.CharField(max_length=255)
    track = models.FileField(upload_to='anthologies/stories/%Y/%m/%d/')
    def __str__(self):
        return self.title[:50]