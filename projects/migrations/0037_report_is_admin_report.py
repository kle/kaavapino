# Generated by Django 2.1.2 on 2018-12-14 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0036_report_reportattribute'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='is_admin_report',
            field=models.BooleanField(default=False, verbose_name='can only be fetched by admin'),
        ),
    ]
