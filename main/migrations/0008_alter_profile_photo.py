# Generated by Django 4.1.3 on 2022-11-30 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_relationship'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='photo',
            field=models.CharField(blank=True, default='main/default_avatar.jpg', max_length=255),
        ),
    ]
