# Generated by Django 4.1.3 on 2022-11-19 11:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Challenge',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True)),
                ('hours', models.IntegerField(default=1)),
                ('reward', models.IntegerField(default=0)),
                ('color', models.CharField(blank=True, default='#B5F2EA', max_length=7)),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='user_creator', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('is_finished', models.BooleanField(default=False)),
                ('type', models.IntegerField(choices=[(1, 'ONEDAY'), (2, 'ROUTINE'), (3, 'CHALLENGETASK'), (4, 'LONGTIME')], default=1)),
            ],
        ),
        migrations.CreateModel(
            name='UserChallenge',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('self_hours', models.IntegerField(default=0)),
                ('is_finished', models.BooleanField(default=False)),
                ('challenge', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.challenge')),
                ('participant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.CharField(blank=True, max_length=255)),
                ('experience', models.IntegerField(blank=True, default=0)),
                ('levels', models.IntegerField(blank=True, default=0)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='challenge',
            name='participants',
            field=models.ManyToManyField(related_name='user_participant', through='main.UserChallenge', to=settings.AUTH_USER_MODEL),
        ),
    ]