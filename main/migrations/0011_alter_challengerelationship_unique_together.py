# Generated by Django 4.1.3 on 2022-12-02 18:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_challengerelationship'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='challengerelationship',
            unique_together={('sender', 'receiver', 'challenge')},
        ),
    ]
