# Generated by Django 5.1 on 2024-08-17 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_user_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='slug',
            field=models.SlugField(default=1, unique=True),
            preserve_default=False,
        ),
    ]
