# Generated by Django 5.0 on 2023-12-11 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo2app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='date',
            field=models.DateField(default='2023-12-11'),
            preserve_default=False,
        ),
    ]