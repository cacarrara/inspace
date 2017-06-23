import uuid

from django.db import models
from django.utils.translation import ugettext_lazy as _


class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Planet(BaseModel):
    name = models.CharField(_('Name'), max_length=250, unique=True)

    class Meta:
        db_table = 'planets'
        ordering = ('name', )
        verbose_name = _('Planet')
        verbose_name_plural = _('Planets')

    def __str__(self):
        return self.name


class Resource(BaseModel):
    title = models.CharField(_('Title'), max_length=250, unique=True)
    description = models.TextField(_('Description'), blank=True)
    planet = models.ForeignKey(Planet, verbose_name=_('Planet'), related_name='resources')

    class Meta:
        db_table = 'resources'
        ordering = ('title', )
        verbose_name = _('Resource')
        verbose_name_plural = _('Resources')

    def __str__(self):
        return self.title
