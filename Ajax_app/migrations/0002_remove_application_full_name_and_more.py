# Generated by Django 5.0.3 on 2024-04-18 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ajax_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='application',
            name='full_name',
        ),
        migrations.RemoveField(
            model_name='application',
            name='resume',
        ),
        migrations.RemoveField(
            model_name='application',
            name='submitted_at',
        ),
        migrations.AddField(
            model_name='application',
            name='education',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='application',
            name='first_name',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='application',
            name='gender',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AddField(
            model_name='application',
            name='last_name',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='application',
            name='course',
            field=models.CharField(max_length=100),
        ),
    ]