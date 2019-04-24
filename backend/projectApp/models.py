from django.db import models
from django.utils.translation import ugettext_lazy as _
from djang.core.validators import MinValueValidator, MaxValueValidator
from django.utils.text import slugify

from tinymce.models import HTMLField


class Project(models.Model):
    """
    Represents project, published on the web-site.
    """

    title = models.CharField(
        _('title'),
        max_length=255,
        unique=True,
        help_text="At most 255 characters."
    )
    slug = models.SlugField(
        _('slug'),
        max_length=128,
        unique=True,
        help_text="At most 128 characters, allowed characters:'-_a-z0-9'."
    )
    preview = models.ImageField(
        _('preview'),
        upload_to='projectApp/previews/',
        blank=True,
        null=True
    )
    short_description = models.TextField(_('short description'))
    full_description = models.HTMLField(_('full description'))
    number_of_people = models.PositiveSmallIntegerField(
        _('number of people'),
        default=1,
        validators=[MinValueValidator(1), MaxValueValidator(1000)],
        help_text="Positive integer in range 1 to 1000 inclusive."
    )
    date_of_created = models.DateTimeField(
        _('date of creation'),
        auto_now_add=True
    )
    date_of_updated = models.DateTimeField(
        _('date of update'),
        auto_now=True
    )
    date_of_end = models.DateTimeField(_('date of end'))
    is_active = models.BooleanFiel(_('is active'), default=True)

    status = models.ForeignKey(
        'Status',
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        verbose_name=_('status')
    )
    tags = models.ManyToManyField(
        'Tag',
        related_name='projects',
        verbose_name=_('tags')
    )

    class Meta:
        verbose_name = "enrolled project"
        verbose_name_plural = "enrolled projects"

    def save(self, *args, **kwargs):
        # Update slug field, if it's empty - write slugified title there:
        self.slug = self.slug.lower() if self.slug else slugify(self.title)

        # Check preview, if it has updated, remove old image:
        try:
            old_self = Project.objects.get(id=self.id)
            if old_self.preview != self.preview:
                old_self.preview.delete(save=False)
        except:
            # If it's a new project or a first preview, just don't do nothing:
            pass

        super().save(*args, **kwargs)

    def __str__(self):
        return "'%s' project." % self.title

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
