# Generated by Django 3.2.7 on 2022-12-27 09:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0005_blog_model_new1_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog_model_new1',
            old_name='user',
            new_name='b_user',
        ),
    ]
