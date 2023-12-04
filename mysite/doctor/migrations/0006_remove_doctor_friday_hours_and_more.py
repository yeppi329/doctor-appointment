# Generated by Django 4.0.3 on 2023-11-29 03:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0005_remove_doctor_non_insurance_services_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doctor',
            name='friday_hours',
        ),
        migrations.RemoveField(
            model_name='doctor',
            name='monday_hours',
        ),
        migrations.RemoveField(
            model_name='doctor',
            name='saturday_hours',
        ),
        migrations.RemoveField(
            model_name='doctor',
            name='sunday_hours',
        ),
        migrations.RemoveField(
            model_name='doctor',
            name='thursday_hours',
        ),
        migrations.RemoveField(
            model_name='doctor',
            name='tuesday_hours',
        ),
        migrations.RemoveField(
            model_name='doctor',
            name='wednesday_hours',
        ),
        migrations.AddField(
            model_name='doctor',
            name='friday_end',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='doctor',
            name='friday_start',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='doctor',
            name='monday_end',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='doctor',
            name='monday_start',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='doctor',
            name='saturday_end',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='doctor',
            name='saturday_start',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='doctor',
            name='sunday_end',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='doctor',
            name='sunday_start',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='doctor',
            name='thursday_end',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='doctor',
            name='thursday_start',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='doctor',
            name='tuesday_end',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='doctor',
            name='tuesday_start',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='doctor',
            name='wednesday_end',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='doctor',
            name='wednesday_start',
            field=models.TimeField(blank=True, null=True),
        ),
    ]