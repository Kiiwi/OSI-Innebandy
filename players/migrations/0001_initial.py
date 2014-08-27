
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Player'
        db.create_table('players_player', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('fornavn', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('etternavn', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('draktnummer', self.gf('django.db.models.fields.IntegerField')(blank=True, null=True)),
            ('posisjon', self.gf('django.db.models.fields.CharField')(blank=True, max_length=10, null=True)),
            ('fødselsdato', self.gf('django.db.models.fields.DateField')()),
            ('profilbilde', self.gf('django.db.models.fields.files.ImageField')(blank=True, max_length=100, null=True)),
        ))
        db.send_create_signal('players', ['Player'])


    def backwards(self, orm):
        # Deleting model 'Player'
        db.delete_table('players_player')


    models = {
        'players.player': {
            'Meta': {'object_name': 'Player'},
            'draktnummer': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'etternavn': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'fornavn': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'fødselsdato': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'posisjon': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '10', 'null': 'True'}),
            'profilbilde': ('django.db.models.fields.files.ImageField', [], {'blank': 'True', 'max_length': '100', 'null': 'True'})
        }
    }

    complete_apps = ['players']