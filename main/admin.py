from django.contrib import admin
from .models import Profile, Challenge, UserChallenge, Task

admin.site.register(Profile)
admin.site.register(Challenge)
admin.site.register(UserChallenge)
admin.site.register(Task)