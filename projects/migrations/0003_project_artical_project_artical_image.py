# Generated by Django 4.2.13 on 2024-07-21 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_rename_blog_artical_project_artical_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='project_artical',
            name='project_artical_image',
            field=models.ImageField(default='default.jpg', upload_to='images/'),
        ),
    ]