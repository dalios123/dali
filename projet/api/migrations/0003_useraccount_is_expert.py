# Generated by Django 4.1.6 on 2023-03-27 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_remove_useraccount_age_useraccount_datedenaissance'),
    ]

    operations = [
        migrations.AddField(
            model_name='useraccount',
            name='is_expert',
            field=models.BooleanField(default=False),
        ),
    ]
