# Generated by Django 3.1.9 on 2021-07-19 11:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resume_page', '0006_auto_20210719_1142'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='education',
            options={'verbose_name_plural': 'Education'},
        ),
        migrations.AlterModelOptions(
            name='interests',
            options={'verbose_name_plural': 'Interests'},
        ),
    ]
