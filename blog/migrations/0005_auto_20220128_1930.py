# Generated by Django 3.2.7 on 2022-01-28 19:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_post_konum'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='title',
            new_name='baslik',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='content',
            new_name='gönderi',
        ),
    ]
