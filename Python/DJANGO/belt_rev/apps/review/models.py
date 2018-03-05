# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from ..login.models import user

class author(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
class book(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    author = models.ForeignKey(author, related_name="books",default=0)
class review(models.Model):
    rating = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    review_txt = models.TextField(max_length=1000, default="none")
    user = models.ForeignKey(user, related_name="u_reviews",default=0)
    book = models.ForeignKey(book, related_name="b_reviews",default=0)
    


