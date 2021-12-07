# Generated by Django 3.2.8 on 2021-12-06 16:38

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Test', '0018_auto_20211204_2321'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('perfiles', '0002_delete_perfil'),
    ]

    operations = [
        migrations.CreateModel(
            name='Certamen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField(default=datetime.datetime(2021, 12, 6, 16, 38, 35, 742300, tzinfo=utc))),
                ('hora', models.TimeField(choices=[('b1', '8:15-9:25'), ('b2', '9:35-10:45'), ('b3', '10:55-12:05'), ('b4', '12:15-13:25'), ('b5', '14:30-15:40'), ('b6', '15:50-17:00'), ('b7', '17:10-18:20'), ('b8', '18:30-19:40'), ('b9', '19:50-21:00'), ('b10', '21:10-22:20')])),
                ('ramo', models.ForeignKey(limit_choices_to={'user_id': '1'}, on_delete=django.db.models.deletion.CASCADE, to='Test.ramo')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]