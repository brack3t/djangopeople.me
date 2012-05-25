# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        db.alter_column('auth_user', 'first_name', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True))

    def backwards(self, orm):
        db.alter_column('auth_user', 'first_name', self.gf('django.db.models.fields.CharField')(max_length=30, blank=True))

    models = {
    }

    complete_apps = ['generic']
