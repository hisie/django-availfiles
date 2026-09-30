import pytest
from django.core.files.uploadedfile import SimpleUploadedFile

from simplefiles.models import SimpleFile

pytestmark = pytest.mark.django_db


def make_file(name="spec-sheet.pdf", content=b"%PDF-1.4 fake"):
    return SimpleUploadedFile(name, content, content_type="application/pdf")


def test_original_filename_is_captured_on_save():
    obj = SimpleFile.objects.create(file=make_file("spec-sheet.pdf"))
    assert obj.original_filename == "spec-sheet.pdf"


def test_display_name_falls_back_to_original_filename():
    obj = SimpleFile.objects.create(file=make_file("spec-sheet.pdf"))
    assert obj.display_name == "spec-sheet.pdf"

    obj.label = "Palmera care sheet"
    assert obj.display_name == "Palmera care sheet"


def test_str_uses_display_name():
    obj = SimpleFile.objects.create(file=make_file("spec-sheet.pdf"), label="Care sheet")
    assert str(obj) == "Care sheet"
