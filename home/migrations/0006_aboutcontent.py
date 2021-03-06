# Generated by Django 2.2.6 on 2019-11-17 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_auto_20191111_1811'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutContent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='about/')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
    ]
