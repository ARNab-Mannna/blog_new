# Generated by Django 3.2.7 on 2022-12-27 09:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0006_rename_user_blog_model_new1_b_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog_model_new1',
            old_name='b_user',
            new_name='user',
        ),
    ]
