# Generated by Django 5.0.2 on 2024-03-10 00:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0020_shopproduct'),
    ]

    operations = [
        migrations.CreateModel(
            name='cartinfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productname1', models.CharField(max_length=50)),
                ('productprice1', models.IntegerField()),
                ('productimage', models.ImageField(upload_to='image/')),
                ('producttotal', models.CharField(max_length=10)),
            ],
        ),
    ]
