# Generated by Django 4.0.8 on 2024-06-14 00:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Brand', '0002_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='brand',
        ),
    ]
