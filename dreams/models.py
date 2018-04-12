# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create dreams model with corresponding attributes.
class Dreams(models.Model):
    dreams_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=150)
    dream_date = models.DateTimeField()
    is_lucid = models.BooleanField()

    class Meta:
        verbose_name = "Dream"
        verbose_name_plural = "Dreams"

    def __unicode__(self):
        return '%s %s %s %s %s' % (self.dreams_id, self.username, self.dream_date, self.is_lucid)