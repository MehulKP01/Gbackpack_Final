# Generated by Django 5.0.2 on 2024-03-14 00:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0023_alter_cartinfo_productquantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartinfo',
            name='productquantity',
            field=models.CharField(default=1, max_length=10),
        ),
    ]