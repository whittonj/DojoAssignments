# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
#No methods in our new manager should ever catch the whole request object with a parameter!!! (just parts, like request.POST)

class courseManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['name']) < 5:
            errors["name"] = "Blog name should be more than 5 characters"
        if len(postData['desc']) < 15:
            errors["desc"] = "Course desc should be more than 15 characters"
        return errors
class course(models.Model):
      name = models.CharField(max_length=255)
      desc = models.CharField(max_length=255)
      created_at = models.DateTimeField(auto_now_add = True)
      updated_at = models.DateTimeField(auto_now = True)
      objects = courseManager()
