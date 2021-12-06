# Generated by Django 3.2.8 on 2021-12-06 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('perfiles', '0002_delete_perfil'),
    ]

    operations = [
        migrations.CreateModel(
            name='Exp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('valor', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Nivel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('numero', models.IntegerField()),
            ],
        ),
    ]