from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to="authors/img/%Y/%m/%d/")
    types = models.TextField()
    deceased = models.BooleanField()

    def __str__(self):
        return self.name[:50]