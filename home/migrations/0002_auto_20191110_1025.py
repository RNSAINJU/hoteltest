# Generated by Django 2.2.6 on 2019-11-10 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imageslider',
            name='description',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='imageslider',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='imageslider',
            name='topic',
            field=models.CharField(blank=True, max_length=10),
        ),
    ]
