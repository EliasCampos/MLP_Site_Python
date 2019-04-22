from django.db import models
from django.utils.translation import ugettext_lazy as _


class Project(models.Model):
    pass


class Tag(models.Model):
    title = models.CharField(
        _("title"),
        max_length=50,
        blank=False,
        unique=True,
        help_text="At most 50 characters."
    )
    slug = models.SlugField(
        _('slug'),
        max_length=50,
        blank=False,
        unique=True,
        help_text="At most 50 characters, allowed characters:'-_a-z0-9'."
    )

    class Meta:
        verbose_name = "project's tag"

    def __str__(self):
        return self.title

class Status(models.Model):
    title = models.CharField(
        _('title'),
        max_length=16,
        unique=True,
        blank=False,
        help_text="At most 16 characters."
    )

    class Meta:
        verbose_name = "project's status"

    def __str__(self):
        return "Status: '%s'." % self.title
