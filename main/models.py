from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.CharField(max_length=255, blank=True, null=False)
    experience = models.IntegerField(blank=True, null=False, default=0)
    levels = models.IntegerField(blank=True, null=False, default=0)

    def __str__(self):
        return self.user.username

class Challenge(models.Model):
    COLOR_CHOICES = [
        ('#ffbe0b', 'Amber'),
        ('#fb5607', 'Orange Pantone'),
        ('#FF006E', 'Winter Sky'),
        ('#8338EC', 'Blue Violet'),
        ('#3A86FF', 'Azure'),
    ]
    creator = models.ForeignKey(User, on_delete=models.PROTECT, related_name='user_creator')
    title = models.CharField(max_length=255, blank=False, null=False)
    description = models.TextField(blank=True, null=False)
    hours = models.IntegerField(blank=False, null=False, default=1)
    participants = models.ManyToManyField(User, through='UserChallenge', related_name='user_participant')
    reward = models.IntegerField(blank=False,null=False, default=0)
    color = models.CharField(max_length=7, choices=COLOR_CHOICES, blank=True, null=False, default='#3A86FF')

    def __str__(self):
        return self.title

class UserChallenge(models.Model):
    participant = models.ForeignKey(User, on_delete=models.CASCADE)
    challenge = models.ForeignKey(Challenge, on_delete=models.CASCADE)
    self_hours = models.IntegerField(null=False, default=0)
    is_finished = models.BooleanField(null=False, default=False)

    def __str__(self):
        return self.participant.username + " : " + self.challenge.title

class Task(models.Model):
    TYPE_CHOICES = [
        (1, 'ONEDAY'),
        (2, 'ROUTINE'),
        (3, 'CHALLENGETASK'),
        (4, 'LONGTIME'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, blank=False, null=False)
    is_finished = models.BooleanField(null=False, default=False)
    type = models.IntegerField(null=False, blank=False, choices=TYPE_CHOICES, default=1)
    def __str__(self):
        return self.user.username + " : " + self.title + " : " + self.get_type_display()
