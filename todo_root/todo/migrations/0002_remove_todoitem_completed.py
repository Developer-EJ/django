# Generated by Django 5.0.4 on 2024-05-16 19:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todoitem',
            name='completed',
        ),
    ]
