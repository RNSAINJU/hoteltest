# Generated by Django 2.2.6 on 2019-11-11 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_backgroundimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='backgroundimage',
            name='name',
            field=models.CharField(blank=True, max_length=10),
        ),
    ]
