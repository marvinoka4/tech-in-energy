# Generated by Django 4.2 on 2023-04-28 14:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_post_h_body_post_h_conclusion_post_h_introduction'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='h_body',
            new_name='body_title',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='h_conclusion',
            new_name='conclusion_title',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='h_introduction',
            new_name='introduction_title',
        ),
    ]