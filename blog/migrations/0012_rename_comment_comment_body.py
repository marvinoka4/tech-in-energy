# Generated by Django 4.2 on 2023-04-24 22:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_rename_conclusion_post_conclusion'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='comment',
            new_name='body',
        ),
    ]
