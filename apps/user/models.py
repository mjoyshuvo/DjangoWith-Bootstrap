from django.db import models
from django.contrib.auth.models import PermissionsMixin, UserManager, AbstractBaseUser, BaseUserManager
from django.contrib.auth.validators import UnicodeUsernameValidator, ASCIIUsernameValidator
from django.utils import six, timezone
from django.utils.translation import ugettext_lazy as _


# Create your models here.


class UserProfileManager(BaseUserManager):
    """Helps Django work with our custom user model."""

    def create_user(self, email, username, password=None):
        """Creates a new user profile."""
        if not email:
            raise ValueError('Users must have an email addresss.')

        email = self.normalize_email(email)
        user = self.model(email=email, username=username, )

        user.set_password(password)
        user.save(using=self._db)
        print('cr')
        return user

    def create_superuser(self, email, username, password):
        """Creates and saves a new superuser with given details."""
        print('csr')
        user = self.create_user(email, username, password)

        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    username_validator = UnicodeUsernameValidator(
    ) if six.PY3 else ASCIIUsernameValidator()

    first_name = models.CharField(null=False, blank=False, max_length=500)
    last_name = models.CharField(null=False, blank=False, max_length=500)
    email = models.EmailField(max_length=255, unique=True)
    username = models.CharField(
        _('username'),
        max_length=150,
        unique=True,
        help_text=_(
            'Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'),
        validators=[username_validator],
        error_messages={
            'unique': _("A user with that username already exists."),
        },
    )
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def get_full_name(self):
        """Django uses this when it needs to get the user's full name."""
        return self.first_name
        # return "{}{}".format(self.first_name, self.last_name)

    def get_username(self):
        """Django uses this when it needs to get the users abbreviated name."""

        return self.username

    def __str__(self):
        """Django uses this when it needs to convert the object to text."""

        return self.email
