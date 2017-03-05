from django.db import models
from django.contrib.auth.models import User

from django.db.models.signals import post_save
from django.dispatch import receiver


class ActiveUsersManager(models.Manager):
    """Active user manager."""

    def get_queryset(self):
        """Get the full query of active users."""
        return super(ActiveUsersManager, self).get_queryset().filter(user__is_active=True)


class UserProfile(models.Model):
    """Profile for the user."""

    objects = models.Manager()
    active = ActiveUsersManager()

    user = models.OneToOneField(
        User,
        related_name="profile",
        on_delete=models.CASCADE
    )
    bio = models.CharField(max_length=500, blank=True, null=True)
    website = models.CharField(max_length=255, blank=True, null=True)

    def is_active(self):
        """Return True if user is active, False if not."""
        return self.user.is_active


@receiver(post_save, sender=User)
def make_profile_for_user(sender, instance, **kwargs):
    """When a user is created, it gets a profile."""
    if kwargs['created']:
        new_profile = UserProfile(user=instance)
        new_profile.save()
