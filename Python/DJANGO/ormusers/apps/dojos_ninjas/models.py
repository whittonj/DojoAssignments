# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

class dojo(models.Model):
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=2)
    desc = models.CharField(max_length=255, default="none")
    
class ninja(models.Model):
      first_name = models.CharField(max_length=255)
      last_name = models.CharField(max_length=255)
      created_at = models.DateTimeField(auto_now_add = True)
      updated_at = models.DateTimeField(auto_now = True)
      dojo = models.ForeignKey(dojo, related_name="ninjas")