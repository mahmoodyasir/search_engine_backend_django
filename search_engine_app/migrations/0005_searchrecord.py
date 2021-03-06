# Generated by Django 4.0.2 on 2022-03-01 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search_engine_app', '0004_everydata_search_count'),
    ]

    operations = [
        migrations.CreateModel(
            name='SearchRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('search_id', models.IntegerField()),
                ('search_value', models.CharField(max_length=200)),
                ('search_date', models.DateField(auto_now_add=True)),
                ('search_time', models.TimeField(auto_now_add=True)),
            ],
        ),
    ]
