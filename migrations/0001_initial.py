# Generated by Django 2.0 on 2018-02-22 01:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255)),
                ('blurb', models.TextField(blank=True, max_length=255)),
                ('num_pages', models.IntegerField(blank=True)),
                ('prince', models.FloatField(blank=True)),
                ('in_print', models.BooleanField(default=True)),
            ],
        ),
    ]
