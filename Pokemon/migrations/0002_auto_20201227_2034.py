# Generated by Django 3.1.4 on 2020-12-27 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pokemon', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemon',
            name='level',
            field=models.IntegerField(),
        ),
    ]
