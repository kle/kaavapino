# Generated by Django 2.0 on 2017-12-21 00:21

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Attribute',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='name')),
                ('value_type', models.CharField(choices=[('int', 'int'), ('string', 'string'), ('boolean', 'boolean'), ('date', 'date')], max_length=64, verbose_name='value type')),
                ('slug', models.SlugField(unique=True, verbose_name='slug')),
            ],
            options={
                'verbose_name': 'attribute',
                'verbose_name_plural': 'attributes',
            },
        ),
        migrations.CreateModel(
            name='AttributeValueChoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=255, verbose_name='value')),
                ('slug', models.SlugField(verbose_name='slug')),
                ('attribute', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='value_choices', to='projects.Attribute', verbose_name='attribute')),
            ],
            options={
                'verbose_name': 'attribute value choice',
                'verbose_name_plural': 'attribute value choices',
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('modified_at', models.DateTimeField(auto_now=True, verbose_name='modified at')),
                ('name', models.CharField(max_length=255, verbose_name='name')),
                ('attribute_data', django.contrib.postgres.fields.jsonb.JSONField(blank=True, default=dict, null=True, verbose_name='attribute data')),
            ],
            options={
                'verbose_name': 'project',
                'verbose_name_plural': 'projects',
            },
        ),
        migrations.CreateModel(
            name='ProjectPhase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='name')),
                ('color', models.CharField(blank=True, max_length=64, verbose_name='color')),
                ('index', models.PositiveIntegerField(blank=True, null=True, verbose_name='index')),
            ],
            options={
                'verbose_name': 'project phase',
                'verbose_name_plural': 'project phases',
            },
        ),
        migrations.CreateModel(
            name='ProjectPhaseAttribute',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('required', models.BooleanField(verbose_name='required')),
                ('index', models.PositiveIntegerField(blank=True, null=True, verbose_name='index')),
                ('attribute', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.Attribute', verbose_name='attribute')),
                ('phase', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.ProjectPhase', verbose_name='phase')),
            ],
            options={
                'verbose_name': 'project phase attribute',
                'verbose_name_plural': 'project phase attributes',
            },
        ),
        migrations.CreateModel(
            name='ProjectType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='name')),
            ],
            options={
                'verbose_name': 'project type',
                'verbose_name_plural': 'project types',
            },
        ),
        migrations.AddField(
            model_name='projectphase',
            name='attributes',
            field=models.ManyToManyField(related_name='project_phases', through='projects.ProjectPhaseAttribute', to='projects.Attribute', verbose_name='attributes'),
        ),
        migrations.AddField(
            model_name='projectphase',
            name='project_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.ProjectType', verbose_name='project type'),
        ),
        migrations.AddField(
            model_name='project',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='projects', to='projects.ProjectType', verbose_name='type'),
        ),
        migrations.AlterUniqueTogether(
            name='projectphase',
            unique_together={('project_type', 'index')},
        ),
        migrations.AlterUniqueTogether(
            name='attributevaluechoice',
            unique_together={('attribute', 'slug')},
        ),
    ]
