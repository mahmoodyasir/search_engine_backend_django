from django.contrib.auth.models import User
from django.db import models


class EveryData(models.Model):
    value = models.CharField(max_length=200, null=False, blank=False)
    description = models.TextField(null=False, blank=False, default=f"This is a description")
    category = models.CharField(max_length=200, null=False, blank=False, default="general")
    search_count = models.IntegerField(default=0)

    def __str__(self):
        return self.value


class SearchRecord(models.Model):
    user_id = models.CharField(max_length=200, null=False, blank=False)
    search_id = models.IntegerField(null=False, blank=False)
    search_value = models.CharField(max_length=200, null=False, blank=False)
    search_date = models.DateField(auto_now_add=True)
    search_time = models.TimeField(auto_now_add=True)

    def __str__(self):
        return self.search_value


