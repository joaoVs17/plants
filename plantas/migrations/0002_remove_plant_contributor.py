# Generated by Django 4.1 on 2022-09-05 04:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('plantas', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='plant',
            name='contributor',
        ),
    ]