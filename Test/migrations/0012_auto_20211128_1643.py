# Generated by Django 3.2.8 on 2021-11-28 19:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Test', '0011_alter_ramo_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='horario',
            name='b1',
            field=models.CharField(choices=[('Ocupado', 'Ocuapado'), ('Libre', 'Libre')], default='Libre', max_length=20),
        ),
        migrations.AlterField(
            model_name='horario',
            name='b10',
            field=models.CharField(choices=[('Ocupado', 'Ocuapado'), ('Libre', 'Libre')], default='Libre', max_length=20),
        ),
        migrations.AlterField(
            model_name='horario',
            name='b2',
            field=models.CharField(choices=[('Ocupado', 'Ocuapado'), ('Libre', 'Libre')], default='Libre', max_length=20),
        ),
        migrations.AlterField(
            model_name='horario',
            name='b3',
            field=models.CharField(choices=[('Ocupado', 'Ocuapado'), ('Libre', 'Libre')], default='Libre', max_length=20),
        ),
        migrations.AlterField(
            model_name='horario',
            name='b4',
            field=models.CharField(choices=[('Ocupado', 'Ocuapado'), ('Libre', 'Libre')], default='Libre', max_length=20),
        ),
        migrations.AlterField(
            model_name='horario',
            name='b5',
            field=models.CharField(choices=[('Ocupado', 'Ocuapado'), ('Libre', 'Libre')], default='Libre', max_length=20),
        ),
        migrations.AlterField(
            model_name='horario',
            name='b6',
            field=models.CharField(choices=[('Ocupado', 'Ocuapado'), ('Libre', 'Libre')], default='Libre', max_length=20),
        ),
        migrations.AlterField(
            model_name='horario',
            name='b7',
            field=models.CharField(choices=[('Ocupado', 'Ocuapado'), ('Libre', 'Libre')], default='Libre', max_length=20),
        ),
        migrations.AlterField(
            model_name='horario',
            name='b8',
            field=models.CharField(choices=[('Ocupado', 'Ocuapado'), ('Libre', 'Libre')], default='Libre', max_length=20),
        ),
        migrations.AlterField(
            model_name='horario',
            name='b9',
            field=models.CharField(choices=[('Ocupado', 'Ocuapado'), ('Libre', 'Libre')], default='Libre', max_length=20),
        ),
        migrations.AlterField(
            model_name='ramo',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Ramos', to=settings.AUTH_USER_MODEL),
        ),
    ]
