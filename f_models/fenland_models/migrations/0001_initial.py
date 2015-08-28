# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('repeat', models.IntegerField(null=True, blank=True)),
                ('studyphase', models.IntegerField(null=True, blank=True)),
                ('appt_date', models.DateField(help_text=b'Format: YYYY-MM-DD', null=True, blank=True)),
                ('appt_time', models.TimeField(help_text=b'Format: HH:MM:SS', null=True, blank=True)),
                ('test_site', models.CharField(max_length=10, blank=True)),
                ('modified_by', models.CharField(max_length=45, blank=True)),
                ('modified', models.DateTimeField(null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='AuditLog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('reason', models.TextField(blank=True)),
                ('edit_date', models.DateField(null=True, blank=True)),
                ('editor', models.CharField(max_length=45, blank=True)),
            ],
            options={
                'verbose_name': 'Audit Log',
                'verbose_name_plural': 'Audit Log',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('curr_status', models.CharField(max_length=45, blank=True)),
            ],
            options={
                'verbose_name': 'Status',
                'verbose_name_plural': 'Status',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Surgery',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('full_name', models.CharField(max_length=45)),
                ('name', models.CharField(max_length=45)),
                ('addr1', models.CharField(max_length=45, blank=True)),
                ('addr2', models.CharField(max_length=45, blank=True)),
                ('town', models.CharField(max_length=45, blank=True)),
                ('county', models.CharField(max_length=45, blank=True)),
                ('postcode', models.CharField(max_length=45, blank=True)),
                ('telephone', models.CharField(max_length=12, blank=True)),
                ('admin_contact_name', models.CharField(max_length=45, blank=True)),
                ('admin_contact_number', models.CharField(max_length=45, blank=True)),
                ('hscic_code', models.CharField(max_length=45, blank=True)),
                ('area', models.CharField(max_length=45, blank=True)),
                ('modified_by', models.CharField(max_length=45, blank=True)),
                ('modified', models.DateTimeField(null=True, blank=True)),
                ('surgeriescol', models.CharField(max_length=45, blank=True)),
                ('latitude', models.FloatField(help_text='Latitude (Lat.) is the angle between any point and the equator (north pole is at 90; south pole is at -90).', null=True, verbose_name='latitude', blank=True)),
                ('longitude', models.FloatField(help_text='Longitude (Long.) is the angle east or west of an arbitrary point on Earth from Greenwich (UK), which is the international zero-longitude point (longitude=0 degrees). The anti-meridian of Greenwich is both 180 (direction to east) and -180 (direction to west).', null=True, verbose_name='longitude', blank=True)),
            ],
            options={
                'verbose_name': 'Surgery',
                'verbose_name_plural': 'Surgeries',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Volunteer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('surname', models.CharField(max_length=45)),
                ('forenames', models.CharField(max_length=45)),
                ('initials', models.CharField(max_length=5, blank=True)),
                ('dob', models.DateField(null=True, blank=True)),
                ('title', models.CharField(blank=True, max_length=12, choices=[(b'Mr', b'Mr'), (b'Mrs', b'Mrs'), (b'Ms', b'Ms'), (b'Miss', b'Miss'), (b'Dr', b'Dr'), (b'Prof', b'Prof')])),
                ('sex', models.CharField(blank=True, max_length=1, choices=[(b'M', b'M'), (b'F', b'F')])),
                ('addr1', models.CharField(max_length=45, blank=True)),
                ('addr2', models.CharField(max_length=45, blank=True)),
                ('town', models.CharField(max_length=45, blank=True)),
                ('county', models.CharField(max_length=45, blank=True)),
                ('postcode', models.CharField(max_length=45, blank=True)),
                ('home_tel', models.CharField(max_length=45, blank=True)),
                ('work_tel', models.CharField(max_length=45, blank=True)),
                ('mobile', models.CharField(max_length=45, blank=True)),
                ('email', models.CharField(max_length=100, blank=True)),
                ('nhs_no', models.CharField(max_length=45, blank=True)),
                ('moved_away', models.IntegerField(blank=True, null=True, choices=[(1, b'True'), (2, b'False'), (3, b'None')])),
                ('diabetes_diagnosed', models.IntegerField(blank=True, null=True, choices=[(1, b'True'), (2, b'False'), (3, b'None')])),
                ('modified_by', models.CharField(max_length=45, blank=True)),
                ('reason', models.IntegerField(null=True, blank=True)),
                ('phase1_comment', models.TextField(blank=True)),
                ('phase2_comment', models.TextField(blank=True)),
                ('modified', models.DateTimeField(null=True, blank=True)),
                ('surgeries', models.ForeignKey(default=4, blank=True, to='fenland_models.Surgery', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='status',
            name='volunteers',
            field=models.ForeignKey(to='fenland_models.Volunteer'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='auditlog',
            name='volunteers',
            field=models.ForeignKey(to='fenland_models.Volunteer'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='appointment',
            name='volunteers',
            field=models.ForeignKey(to='fenland_models.Volunteer'),
            preserve_default=True,
        ),
    ]
