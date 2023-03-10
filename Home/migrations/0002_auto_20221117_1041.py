# Generated by Django 3.2.7 on 2022-11-17 05:11

from django.db import migrations, models
import froala_editor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='blog_model_new1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=1000)),
                ('content', froala_editor.fields.FroalaField()),
                ('slug', models.SlugField(max_length=1000)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('update_to', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.DeleteModel(
            name='blog_model',
        ),
    ]
