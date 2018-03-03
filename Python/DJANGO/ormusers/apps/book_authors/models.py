# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
class Author(models.Model):
      first_name = models.CharField(max_length=255)
      last_name = models.CharField(max_length=255)
      email = models.CharField(max_length=255)
      created_at = models.DateTimeField(auto_now_add = True)
      updated_at = models.DateTimeField(auto_now = True)
class book(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    desc = models.TextField(max_length=1000, default="none")
    Author = models.ForeignKey(Author, related_name="books",default=0)
    
