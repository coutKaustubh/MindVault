from django.db import models
# Create your models here.
class VaultEntry(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    topic_image = models.ImageField(upload_to='images')