from django.db import models

class People(models.Model):
    name = models.CharField(max_length=256, null=False, blank=False)
    email = models.EmailField(max_length=256, null=False, blank=False, default="SRM Email only**")
    instagram = models.CharField(max_length=256, null=True, blank=True, default="only the id without '@' or link")
    snapchat = models.CharField(max_length=256, null=True, blank=True)
    others = models.TextField(null=True, blank=True)
