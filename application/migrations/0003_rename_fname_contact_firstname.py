# Generated by Django 5.0.2 on 2024-03-01 01:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0002_rename_firstname_contact_fname'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='fname',
            new_name='firstname',
        ),
    ]
