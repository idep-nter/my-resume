# Generated by Django 3.1.9 on 2021-07-19 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume_page', '0007_auto_20210719_1145'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='experience',
            options={'verbose_name_plural': 'Experience'},
        ),
        migrations.AddField(
            model_name='author',
            name='about_me',
            field=models.TextField(null=True),
        ),
    ]