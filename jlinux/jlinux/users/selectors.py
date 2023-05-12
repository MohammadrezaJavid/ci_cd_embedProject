from .models import Profile, BaseUser
from django.db.models import QuerySet

def get_profile(user:BaseUser) -> QuerySet[Profile]:
    return Profile.objects.get(user=user)
