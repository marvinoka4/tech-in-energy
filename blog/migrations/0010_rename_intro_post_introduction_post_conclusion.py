# Generated by Django 4.2 on 2023-04-24 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_post_intro'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='intro',
            new_name='introduction',
        ),
        migrations.AddField(
            model_name='post',
            name='Conclusion',
            field=models.TextField(default='Conclusion'),
        ),
    ]
