# Generated by Django 4.0.2 on 2022-02-28 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search_engine_app', '0002_alter_everydata_category_alter_everydata_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='everydata',
            name='category',
            field=models.CharField(default='general', max_length=200),
        ),
        migrations.AlterField(
            model_name='everydata',
            name='description',
            field=models.TextField(default='This is a description'),
        ),
    ]
