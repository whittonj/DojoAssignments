# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.db import models
import bcrypt

class usersManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['first_name']) < 3:
            errors["fname"] = "First name should be more than 2 characters"
        if not (postData['first_name']).isalpha():
            errors["fnamel"] = "First name can only be characters"
        if len(postData['last_name']) < 3:
            errors["lname"] = "Last name should be more than 2 characters"
        if not postData['last_name'].isalpha():
            errors["fnamel"] = "Lasst name can only be characters"
        try:
            validate_email(postData['email_address'])
        except ValidationError as e:
           errors["email"] = "Email must be valid"
        if len(postData['pass']) < 8:
            errors["pass_l"] = "Password must be 8 characters"
        if (postData['pass'] !=  postData['c_pass']):
            errors["pass_m"] = "Password fields must match"
        return errors
    def login_try(self, postData):
        errors = {}
        try:
            users.objects.get(email_address = postData['login_address']) 
            return errors
        except:
            errors["email"] = "Email not in DB"
            return errors
    def pw_match(self, postData):
        errors = {}
        usr = users.objects.get(email_address = postData['login_address'])
        usr_pw = usr.password
        post_pw=postData['pw']
        if bcrypt.checkpw(post_pw.encode(), usr_pw.encode()): 
            return errors
        else:
            errors["email"] = "Wrong password"
            return errors

class users(models.Model):
      first_name = models.CharField(max_length=255)
      last_name = models.CharField(max_length=255)
      email_address = models.CharField(max_length=255)
      password = models.CharField(max_length=255)
      created_at = models.DateTimeField(auto_now_add = True)
      updated_at = models.DateTimeField(auto_now = True)
      objects = usersManager()
