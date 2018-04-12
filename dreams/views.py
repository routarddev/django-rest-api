# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework import viewsets

from .models import Dreams
from .serializers import DreamsSerializer

class DreamViewSet(viewsets.ModelViewSet):
    queryset = Dreams.objects.all()
    serializer_class = DreamsSerializer
