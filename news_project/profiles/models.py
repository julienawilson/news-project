from django.db import models
from django.contrib.auth.models import User


class ActiveUsersManager(models.Manager):
    """Active user manager."""

    def get_queryset(self):
        """Get the full query of active users."""
        return super(ActiveUsersManager, self).get_queryset().filter(user__is_active=True)


class UserProfile(models.Model):
    """Profile for the user."""

    objects = models.Manager()
    active = ActiveUsersManager()

    user = models.OneToOneFiels(
        User,
        related_name="profile",
        on_delete=models.CASCADE
    )
    