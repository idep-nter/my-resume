# Generated by Django 3.1.9 on 2021-07-19 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume_page', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='tel',
            field=models.IntegerField(),
        ),
    ]
