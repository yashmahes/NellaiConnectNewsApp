# Generated by Django 2.1.7 on 2019-02-15 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_auto_20190215_2035'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsdescription',
            name='nonheading',
            field=models.CharField(blank=True, max_length=5550),
        ),
    ]
