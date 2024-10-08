from django.db import models

class tagdescription(models.Model):
    title = models.CharField(max_length=255)
    image = models.URLField(max_length=1024)
    tags = models.TextField()
    description = models.TextField()

