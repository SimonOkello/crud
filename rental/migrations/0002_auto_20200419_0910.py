# Generated by Django 3.0.5 on 2020-04-19 06:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rental', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='borrowed',
            name='owner',
        ),
        migrations.RemoveField(
            model_name='friend',
            name='owner',
        ),
    ]