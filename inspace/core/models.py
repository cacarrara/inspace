import uuid

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.text import slugify

from . import utils


class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class SlugModelMixin(models.Model):
    slug = models.SlugField(
        _('Slug Title'),
        max_length=250,
        unique=True,
        blank=True,
        null=True
    )

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    class Meta:
        abstract = True


class Planet(BaseModel):
    name = models.CharField(_('Name'), max_length=250, unique=True)

    class Meta:
        db_table = 'planets'
        ordering = ('-updated_at', 'name')
        verbose_name = _('Planet')
        verbose_name_plural = _('Planets')

    def __str__(self):
        return self.name


class Resource(SlugModelMixin, BaseModel):
    title = models.CharField(_('Title'), max_length=250, unique=True)
    description = models.TextField(_('Description'), blank=True)
    planet = models.ForeignKey(Planet, verbose_name=_('Planet'), related_name='resources')

    class Meta:
        db_table = 'resources'
        ordering = ('-updated_at', 'title')
        verbose_name = _('Resource')
        verbose_name_plural = _('Resources')

    def is_link(self):
        return False

    def __str__(self):
        return self.title


class ResourceLink(SlugModelMixin, BaseModel):
    url = models.URLField(_("Url"), unique=True)
    title = models.CharField(_('Title'), max_length=250, unique=True)
    description = models.TextField(_('Description'), blank=True)
    planet = models.ForeignKey(Planet, verbose_name=_('Planet'), related_name='resources_links')

    class Meta:
        db_table = 'resources_links'
        ordering = ('-updated_at', 'title')
        verbose_name = _('Resource Link')
        verbose_name_plural = _('Resources Links')

    def is_link(self):
        return True

    def save(self, *args, **kwargs):
        if self.url:
            self.description = utils.get_site_description(self.url)
        if not self.description:
            self.description = self.title
        return super().save(*args, **kwargs)

    def __str__(self):
        return '{} <{}>'.format(self.title, self.url)
