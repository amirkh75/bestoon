# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Expensee , income , Token



admin.site.register(Expensee)
admin.site.register(income)
admin.site.register(Token)
