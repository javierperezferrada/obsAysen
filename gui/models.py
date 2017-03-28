from __future__ import unicode_literals

from django.db import models

class News(models.Model):
    title = models.CharField(max_length=500)
    resumen = models.CharField(max_length=5000)
    content = models.CharField(max_length=10000)
    imagen = models.FileField(upload_to='news/')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
    	ordering = ["-created_at"]


class Report(models.Model):
    title = models.CharField(max_length=500)
    fileReport = models.FileField(upload_to='reports/')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
    	ordering = ["-created_at"]