# Generated by Django 2.1.4 on 2019-01-22 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0048_projectattributefile_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectcomment',
            name='generated',
            field=models.BooleanField(default=False, verbose_name='generated'),
        ),
    ]
