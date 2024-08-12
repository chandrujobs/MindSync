from django.contrib import admin
from .models import UserProfile, Session, MentalHealthResource, ChatHistory

admin.site.register(UserProfile)
admin.site.register(Session)
admin.site.register(MentalHealthResource)
admin.site.register(ChatHistory)
