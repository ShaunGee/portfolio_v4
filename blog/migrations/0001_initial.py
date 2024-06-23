# Generated by Django 4.2.13 on 2024-06-22 23:41

from django.db import migrations, models
import django_ckeditor_5.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project_artical',
            fields=[
                ('blog_id', models.AutoField(primary_key=True, serialize=False)),
                ('blog_title', models.CharField(max_length=100)),
                ('blog_subheadeing', models.CharField(max_length=200)),
                ('blog_body', django_ckeditor_5.fields.CKEditor5Field(verbose_name='Text')),
            ],
        ),
    ]
