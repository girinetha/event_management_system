# Generated by Django 4.0.2 on 2022-05-02 11:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eventapp', '0013_rename_titel_review_title'),
    ]

    operations = [
        migrations.RenameField(
            model_name='addevent',
            old_name='venueaddress',
            new_name='venueaddres',
        ),
    ]
