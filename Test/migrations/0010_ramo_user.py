# Generated by Django 3.2.8 on 2021-11-28 17:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Test', '0009_horario_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='ramo',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Ramos', to=settings.AUTH_USER_MODEL),
        ),
    ]
