# Generated by Django 4.0.3 on 2023-11-29 00:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doctor',
            name='operating_hours',
        ),
        migrations.AddField(
            model_name='doctor',
            name='friday_hours',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='doctor',
            name='monday_hours',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='doctor',
            name='saturday_hours',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='doctor',
            name='sunday_hours',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='doctor',
            name='thursday_hours',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='doctor',
            name='tuesday_hours',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='doctor',
            name='wednesday_hours',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
