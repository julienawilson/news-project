"""Tests for Profile App."""
from django.test import TestCase
from django.contrib.auth.models import User
from profiles.models import UserProfile

import factory


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User
    username = factory.Sequence(lambda n: "Imgr User {}".format(n))
    email = factory.LazyAttribute(
        lambda x: "{}@datsite.com".format(x.username.replace(" ", ""))
    )


class ProfileCase(TestCase):
    """The Profile Model Test Runner."""

    def setUp(self):
        """DB setup for tests."""
        self.users = [UserFactory.create() for i in range(10)]

    def test_profile_made_when_user_saved(self):
        """Test that making a user also makes a profile."""
        self.assertTrue(UserProfile.objects.count() == 10)

    def test_profile_same_data_as_user(self):
        """Test that the profile has the same data as the user."""
        uid = User.objects.first().id
        self.assertTrue(UserProfile.objects.filter(id=uid).first().user.username == User.objects.first().username)

    def test_delete_user_cascades(self):
        """Test that deleting a User deletes the Profile."""
        uid = User.objects.first().id
        test_user = User.objects.filter(id=uid).first()
        test_user.delete()
        self.assertTrue(len(UserProfile.objects.filter(id=uid)) == 0)  # this is a weird test

    def test_delete_user_cascades_model_len(self):
        """Test that deleting a User deletes the Profile in the model length."""
        uid = User.objects.first().id
        test_user = User.objects.filter(id=uid).first()  # this could be different
        test_user.delete()
        self.assertTrue(len(UserProfile.objects.all()) == 9)

    def test_profile_model_is_active(self):
        """Test that the profile isactive param is true."""
        self.assertTrue(UserProfile.objects.first().is_active)

    # def test_profile_string_method_object_not_in(self):
    #     """Test that the string representation doesn't contain "object"."""
    #     profile = UserProfile.objects.first()
    #     self.assertNotIn("object", str(profile))

    # def test_profile_string_method_returns_string(self):
    #     """Test that the string representation is a string."""
    #     profile = UserProfile.objects.first()
    #     self.assertIsInstance(str(profile), str)

    def test_active_returns_only_active_profiles(self):
        """Test active method returns only active profiles queryset."""
        this_user = User.objects.all()[0]
        this_user.is_active = False
        this_user.save()
        self.assertEqual(UserProfile.active.count(), UserProfile.objects.count() - 1)

    def test_profile_is_active_returns_user_is_active(self):
        """Test active method on profile is same as user."""
        this_user = User.objects.all()[0]
        this_user.is_active = False
        this_user.save()
        self.assertFalse(this_user.profile.is_active())

    def test_change_profile_changes_user_profile(self):
        """Test changes on profile mean changes on user profile as well."""
        this_profile = UserProfile.objects.first()
        this_profile.bio = "random bio"
        this_profile.save()
        this_user = User.objects.first()
        self.assertTrue(this_user.profile.bio == this_profile.bio)
