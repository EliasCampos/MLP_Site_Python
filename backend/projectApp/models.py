from django.db import models
from django.utils.translation import ugettext_lazy as _


class Project(models.Model):
    pass


class Tag(models.Model):
    """ Represents tag which marks programming language or technology,
        used in some project. Project can have many tags, so it has
        one to many relation with Project model. """

    title = models.CharField(
        _('title'),
        max_length=50,
        unique=True,
        help_text="At most 50 characters."
    )
    slug = models.SlugField(
        _('slug'),
        max_length=50,
        unique=True,
        help_text="At most 50 characters, allowed characters:'-_a-z0-9'."
    )

    class Meta:
        verbose_name = "project's tag"
        verbose_name_plural = "project's tags"

    def save(self, *args, **kwargs):
        """ Before storing data in database,
        converts slug string to lower case. """

        self.slug = self.slug.lower()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

class Status(models.Model):
    """ Represents status of some project. (for ex. 'active', 'complete') """

    title = models.CharField(
        _('title'),
        max_length=16,
        unique=True,
        help_text="At most 16 characters."
    )

    class Meta:
        verbose_name = "project's status"
        verbose_name_plural = "project's statuses"

    def __str__(self):
        return "Status: '%s'." % self.title
