# Generated by Django 4.0.4 on 2022-05-28 09:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('LSED', '0006_alter_studentextra_photo_alter_teacherextra_photo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studentextra',
            name='photo',
        ),
        migrations.RemoveField(
            model_name='teacherextra',
            name='photo',
        ),
    ]