# Generated by Django 3.2.8 on 2021-11-22 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Test', '0005_rename_horario_ocupado_horario'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ramo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
            ],
        ),
        migrations.AlterField(
            model_name='horario',
            name='b1',
            field=models.CharField(choices=[('ocupado', 'Ocupado'), ('libre', 'Libre')], default='libre', max_length=20),
        ),
        migrations.AlterField(
            model_name='horario',
            name='b10',
            field=models.CharField(choices=[('ocupado', 'Ocupado'), ('libre', 'Libre')], default='libre', max_length=20),
        ),
        migrations.AlterField(
            model_name='horario',
            name='b2',
            field=models.CharField(choices=[('ocupado', 'Ocupado'), ('libre', 'Libre')], default='libre', max_length=20),
        ),
        migrations.AlterField(
            model_name='horario',
            name='b3',
            field=models.CharField(choices=[('ocupado', 'Ocupado'), ('libre', 'Libre')], default='libre', max_length=20),
        ),
        migrations.AlterField(
            model_name='horario',
            name='b4',
            field=models.CharField(choices=[('ocupado', 'Ocupado'), ('libre', 'Libre')], default='libre', max_length=20),
        ),
        migrations.AlterField(
            model_name='horario',
            name='b5',
            field=models.CharField(choices=[('ocupado', 'Ocupado'), ('libre', 'Libre')], default='libre', max_length=20),
        ),
        migrations.AlterField(
            model_name='horario',
            name='b6',
            field=models.CharField(choices=[('ocupado', 'Ocupado'), ('libre', 'Libre')], default='libre', max_length=20),
        ),
        migrations.AlterField(
            model_name='horario',
            name='b7',
            field=models.CharField(choices=[('ocupado', 'Ocupado'), ('libre', 'Libre')], default='libre', max_length=20),
        ),
        migrations.AlterField(
            model_name='horario',
            name='b8',
            field=models.CharField(choices=[('ocupado', 'Ocupado'), ('libre', 'Libre')], default='libre', max_length=20),
        ),
        migrations.AlterField(
            model_name='horario',
            name='b9',
            field=models.CharField(choices=[('ocupado', 'Ocupado'), ('libre', 'Libre')], default='libre', max_length=20),
        ),
    ]
