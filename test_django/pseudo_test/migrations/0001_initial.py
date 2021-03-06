# Generated by Django 2.2 on 2019-04-22 19:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.TextField()),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('test_in', models.TextField(default='[]')),
                ('test_out', models.TextField(default='[]')),
                ('task_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pseudo_test.Task')),
            ],
        ),
        migrations.CreateModel(
            name='Score',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_id', models.TextField()),
                ('score_date', models.DateTimeField()),
                ('score', models.IntegerField()),
                ('task_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pseudo_test.Task')),
            ],
        ),
    ]
