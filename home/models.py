from django.db import models

class product(models.Model):
    name = models.CharField(max_length=256, null=False, blank=False)
    instagram = models.CharField(max_length=256, null=True, blank=True)
    snapchat = models.CharField(max_length=256, null=True, blank=True)
    others = models.TextField(null=True, blank=True)
