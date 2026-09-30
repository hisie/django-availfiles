import os

from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _


class AvailFile(models.Model):
    """A flat file library — deliberately *not* related to any other
    model (no FK from a Post/Product/whatever to this). The whole point
    is a place to upload a file once and link to it from anywhere (a
    blog post body, a product description, ...) via its plain URL,
    rather than a structured per-model attachment relation.

    No opinion here about which file types are allowed — that's a
    deployment policy (e.g. "images go through the existing drag-and-drop
    upload flow, this library is for everything else"), enforced by
    whichever integration layer's upload view is actually used (see
    django-oscar-availfiles), not baked into this model.
    """

    file = models.FileField(_("file"), upload_to="availfiles/%Y/%m/%d/")
    original_filename = models.CharField(_("original filename"), max_length=255, editable=False)
    label = models.CharField(
        _("label"), max_length=255, blank=True, help_text=_("Optional — defaults to the filename.")
    )

    uploaded_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name=_("uploaded by"),
        related_name="availfiles",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    uploaded_at = models.DateTimeField(_("uploaded at"), auto_now_add=True)

    class Meta:
        ordering = ("-uploaded_at",)
        verbose_name = _("file")
        verbose_name_plural = _("files")

    def __str__(self) -> str:
        return self.display_name

    def save(self, *args, **kwargs):
        if not self.original_filename and self.file:
            self.original_filename = os.path.basename(self.file.name)
        super().save(*args, **kwargs)

    @property
    def display_name(self) -> str:
        return self.label or self.original_filename
