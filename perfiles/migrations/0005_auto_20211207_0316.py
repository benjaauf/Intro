# Generated by Django 3.2.8 on 2021-12-07 06:16

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Test', '0019_alter_ramo_dificultad'),
        ('perfiles', '0004_auto_20211206_1635'),
    ]

    operations = [
        migrations.AlterField(
            model_name='certamen',
            name='fecha',
            field=models.DateField(default=datetime.date(2021, 12, 7)),
        ),
        migrations.AlterField(
            model_name='certamen',
            name='ramo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Test.ramo'),
        ),
    ]
