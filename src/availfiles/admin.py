from django.contrib import admin

from availfiles.models import AvailFile


@admin.register(AvailFile)
class AvailFileAdmin(admin.ModelAdmin):
    list_display = ("display_name", "original_filename", "uploaded_by", "uploaded_at")
    search_fields = ("label", "original_filename")
    readonly_fields = ("original_filename", "uploaded_at")
