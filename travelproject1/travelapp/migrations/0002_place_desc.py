# Generated by Django 4.2.6 on 2023-10-12 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travelapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='place',
            name='desc',
            field=models.TextField(default='', verbose_name=''),
            preserve_default=False,
        ),
    ]
