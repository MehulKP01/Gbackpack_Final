# Generated by Django 5.0.2 on 2024-03-05 01:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0008_delete_login_data'),
    ]

    operations = [
        migrations.RenameField(
            model_name='register_data',
            old_name='name',
            new_name='username',
        ),
        migrations.RenameField(
            model_name='register_data',
            old_name='password',
            new_name='userpassword',
        ),
    ]
