# Generated by Django 2.2.5 on 2019-10-13 05:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_auto_20191012_2233'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userinfo',
            old_name='aboutme',
            new_name='about_me',
        ),
    ]