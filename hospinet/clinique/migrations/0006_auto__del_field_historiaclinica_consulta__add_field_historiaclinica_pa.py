# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Deleting field 'HistoriaClinica.consulta'
        db.delete_column('clinique_historiaclinica', 'consulta_id')

        # Adding field 'HistoriaClinica.paciente'
        db.add_column('clinique_historiaclinica', 'paciente', self.gf('django.db.models.fields.related.ForeignKey')(related_name='historias_clinicas', null=True, to=orm['clinique.Paciente']), keep_default=False)

        # Changing field 'Optometria.d_p_ojo_izquierdo'
        db.alter_column('clinique_optometria', 'd_p_ojo_izquierdo', self.gf('django.db.models.fields.DecimalField')(max_digits=5, decimal_places=2))

        # Changing field 'Optometria.esfera_ojo_derecho'
        db.alter_column('clinique_optometria', 'esfera_ojo_derecho', self.gf('django.db.models.fields.DecimalField')(max_digits=5, decimal_places=2))

        # Changing field 'Optometria.cilindro_ojo_derecho'
        db.alter_column('clinique_optometria', 'cilindro_ojo_derecho', self.gf('django.db.models.fields.DecimalField')(max_digits=5, decimal_places=2))

        # Changing field 'Optometria.adicion_ojo_izquierdo'
        db.alter_column('clinique_optometria', 'adicion_ojo_izquierdo', self.gf('django.db.models.fields.DecimalField')(max_digits=5, decimal_places=2))

        # Changing field 'Optometria.esfera_ojo_izquierdo'
        db.alter_column('clinique_optometria', 'esfera_ojo_izquierdo', self.gf('django.db.models.fields.DecimalField')(max_digits=5, decimal_places=2))

        # Changing field 'Optometria.altura_ojo_izquierdo'
        db.alter_column('clinique_optometria', 'altura_ojo_izquierdo', self.gf('django.db.models.fields.DecimalField')(max_digits=5, decimal_places=2))

        # Changing field 'Optometria.altura_ojo_derecho'
        db.alter_column('clinique_optometria', 'altura_ojo_derecho', self.gf('django.db.models.fields.DecimalField')(max_digits=5, decimal_places=2))

        # Changing field 'Optometria.adicion_ojo_derecho'
        db.alter_column('clinique_optometria', 'adicion_ojo_derecho', self.gf('django.db.models.fields.DecimalField')(max_digits=5, decimal_places=2))

        # Changing field 'Optometria.eje_ojo_izquierdo'
        db.alter_column('clinique_optometria', 'eje_ojo_izquierdo', self.gf('django.db.models.fields.DecimalField')(max_digits=5, decimal_places=2))

        # Changing field 'Optometria.cilindro_ojo_izquierdo'
        db.alter_column('clinique_optometria', 'cilindro_ojo_izquierdo', self.gf('django.db.models.fields.DecimalField')(max_digits=5, decimal_places=2))

        # Changing field 'Optometria.eje_ojo_derecho'
        db.alter_column('clinique_optometria', 'eje_ojo_derecho', self.gf('django.db.models.fields.DecimalField')(max_digits=5, decimal_places=2))

        # Changing field 'Optometria.prisma_ojo_izquierdo'
        db.alter_column('clinique_optometria', 'prisma_ojo_izquierdo', self.gf('django.db.models.fields.DecimalField')(max_digits=5, decimal_places=2))

        # Changing field 'Optometria.prisma_ojo_derecho'
        db.alter_column('clinique_optometria', 'prisma_ojo_derecho', self.gf('django.db.models.fields.DecimalField')(max_digits=5, decimal_places=2))

        # Changing field 'Optometria.d_p_ojo_derecho'
        db.alter_column('clinique_optometria', 'd_p_ojo_derecho', self.gf('django.db.models.fields.DecimalField')(max_digits=5, decimal_places=2))


    def backwards(self, orm):
        
        # User chose to not deal with backwards NULL issues for 'HistoriaClinica.consulta'
        raise RuntimeError("Cannot reverse this migration. 'HistoriaClinica.consulta' and its values cannot be restored.")

        # Deleting field 'HistoriaClinica.paciente'
        db.delete_column('clinique_historiaclinica', 'paciente_id')

        # Changing field 'Optometria.d_p_ojo_izquierdo'
        db.alter_column('clinique_optometria', 'd_p_ojo_izquierdo', self.gf('django.db.models.fields.IntegerField')())

        # Changing field 'Optometria.esfera_ojo_derecho'
        db.alter_column('clinique_optometria', 'esfera_ojo_derecho', self.gf('django.db.models.fields.IntegerField')())

        # Changing field 'Optometria.cilindro_ojo_derecho'
        db.alter_column('clinique_optometria', 'cilindro_ojo_derecho', self.gf('django.db.models.fields.IntegerField')())

        # Changing field 'Optometria.adicion_ojo_izquierdo'
        db.alter_column('clinique_optometria', 'adicion_ojo_izquierdo', self.gf('django.db.models.fields.IntegerField')())

        # Changing field 'Optometria.esfera_ojo_izquierdo'
        db.alter_column('clinique_optometria', 'esfera_ojo_izquierdo', self.gf('django.db.models.fields.IntegerField')())

        # Changing field 'Optometria.altura_ojo_izquierdo'
        db.alter_column('clinique_optometria', 'altura_ojo_izquierdo', self.gf('django.db.models.fields.IntegerField')())

        # Changing field 'Optometria.altura_ojo_derecho'
        db.alter_column('clinique_optometria', 'altura_ojo_derecho', self.gf('django.db.models.fields.IntegerField')())

        # Changing field 'Optometria.adicion_ojo_derecho'
        db.alter_column('clinique_optometria', 'adicion_ojo_derecho', self.gf('django.db.models.fields.IntegerField')())

        # Changing field 'Optometria.eje_ojo_izquierdo'
        db.alter_column('clinique_optometria', 'eje_ojo_izquierdo', self.gf('django.db.models.fields.IntegerField')())

        # Changing field 'Optometria.cilindro_ojo_izquierdo'
        db.alter_column('clinique_optometria', 'cilindro_ojo_izquierdo', self.gf('django.db.models.fields.IntegerField')())

        # Changing field 'Optometria.eje_ojo_derecho'
        db.alter_column('clinique_optometria', 'eje_ojo_derecho', self.gf('django.db.models.fields.IntegerField')())

        # Changing field 'Optometria.prisma_ojo_izquierdo'
        db.alter_column('clinique_optometria', 'prisma_ojo_izquierdo', self.gf('django.db.models.fields.IntegerField')())

        # Changing field 'Optometria.prisma_ojo_derecho'
        db.alter_column('clinique_optometria', 'prisma_ojo_derecho', self.gf('django.db.models.fields.IntegerField')())

        # Changing field 'Optometria.d_p_ojo_derecho'
        db.alter_column('clinique_optometria', 'd_p_ojo_derecho', self.gf('django.db.models.fields.IntegerField')())


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2012, 6, 12, 9, 9, 23, 437284)'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2012, 6, 12, 9, 9, 23, 437137)'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'clinique.cita': {
            'Meta': {'object_name': 'Cita'},
            'consultorio': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'citas'", 'to': "orm['clinique.Consultorio']"}),
            'fecha_y_hora': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2012, 6, 12, 9, 9, 21, 152484)'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'clinique.consulta': {
            'Meta': {'object_name': 'Consulta'},
            'fecha_y_hora': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'paciente': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'consultas'", 'to': "orm['clinique.Paciente']"}),
            'razon_de_la_visita': ('django.db.models.fields.TextField', [], {'blank': 'True'})
        },
        'clinique.consultorio': {
            'Meta': {'object_name': 'Consultorio'},
            'doctor': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'consultorios'", 'null': 'True', 'to': "orm['users.Profile']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'secretaria': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'secretariados'", 'null': 'True', 'to': "orm['users.Profile']"}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '36', 'blank': 'True'})
        },
        'clinique.esperador': {
            'Meta': {'object_name': 'Esperador'},
            'atendido': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'consultorio': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'esperadores'", 'to': "orm['clinique.Consultorio']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'paciente': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'esperas'", 'to': "orm['clinique.Paciente']"})
        },
        'clinique.historiaclinica': {
            'Meta': {'object_name': 'HistoriaClinica'},
            'agudeza_visual_ojo_derecho': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'agudeza_visual_ojo_izquierdo': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'fecha_y_hora': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nota': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'paciente': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'historias_clinicas'", 'null': 'True', 'to': "orm['clinique.Paciente']"})
        },
        'clinique.optometria': {
            'Meta': {'object_name': 'Optometria'},
            'adicion_ojo_derecho': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '5', 'decimal_places': '2'}),
            'adicion_ojo_izquierdo': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '5', 'decimal_places': '2'}),
            'altura_ojo_derecho': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '5', 'decimal_places': '2'}),
            'altura_ojo_izquierdo': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '5', 'decimal_places': '2'}),
            'cilindro_ojo_derecho': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '5', 'decimal_places': '2'}),
            'cilindro_ojo_izquierdo': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '5', 'decimal_places': '2'}),
            'd_p_ojo_derecho': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '5', 'decimal_places': '2'}),
            'd_p_ojo_izquierdo': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '5', 'decimal_places': '2'}),
            'eje_ojo_derecho': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '5', 'decimal_places': '2'}),
            'eje_ojo_izquierdo': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '5', 'decimal_places': '2'}),
            'esfera_ojo_derecho': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '5', 'decimal_places': '2'}),
            'esfera_ojo_izquierdo': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '5', 'decimal_places': '2'}),
            'fecha_y_hora': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'paciente': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'optometrias'", 'to': "orm['clinique.Paciente']"}),
            'prisma_ojo_derecho': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '5', 'decimal_places': '2'}),
            'prisma_ojo_izquierdo': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '5', 'decimal_places': '2'})
        },
        'clinique.paciente': {
            'Meta': {'object_name': 'Paciente'},
            'consultorio': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'pacientes'", 'to': "orm['clinique.Consultorio']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'persona': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'consultorios'", 'to': "orm['persona.Persona']"}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '36', 'blank': 'True'})
        },
        'clinique.receta': {
            'Meta': {'object_name': 'Receta'},
            'fecha_y_hora': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'medicamentos': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'notas_adicionales': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'paciente': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'recetas'", 'to': "orm['clinique.Paciente']"})
        },
        'clinique.transaccion': {
            'Meta': {'object_name': 'Transaccion'},
            'concepto': ('django.db.models.fields.CharField', [], {'max_length': '1', 'blank': 'True'}),
            'fecha_y_hora': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'monto': ('django.db.models.fields.DecimalField', [], {'max_digits': '12', 'decimal_places': '2'}),
            'paciente': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'transacciones'", 'to': "orm['clinique.Paciente']"}),
            'tipo': ('django.db.models.fields.IntegerField', [], {})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'persona.persona': {
            'Meta': {'object_name': 'Persona'},
            'antiguedad': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'apellido': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'cargo': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'celular': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'centro_trabajo': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'ci': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'direccion_trabajo': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'domicilio': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'estado_civil': ('django.db.models.fields.CharField', [], {'max_length': '1', 'blank': 'True'}),
            'fax': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'fotografia': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'identificacion': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'nacimiento': ('django.db.models.fields.DateField', [], {'default': 'datetime.date.today'}),
            'nacionalidad': ('persona.fields.OrderedCountryField', [], {'max_length': '2', 'blank': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'profesion': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'sexo': ('django.db.models.fields.CharField', [], {'max_length': '1', 'blank': 'True'}),
            'tel_trabajo': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'telefono': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'tipo_identificacion': ('django.db.models.fields.CharField', [], {'max_length': '1', 'blank': 'True'})
        },
        'users.profile': {
            'Meta': {'object_name': 'Profile'},
            'doctor': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'suscripcion': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime.now'}),
            'suscriptor': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'dependientes'", 'null': 'True', 'to': "orm['auth.User']"}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['auth.User']", 'unique': 'True', 'primary_key': 'True'})
        }
    }

    complete_apps = ['clinique']