# Generated by Django 3.0.5 on 2020-04-26 14:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rental', '0002_auto_20200419_0910'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='borrowed',
            options={'verbose_name_plural': 'Borrowed Items'},
        ),
    ]
