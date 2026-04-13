from django.urls import path
from .views import (
    viewAll,
    note_detail,
    createNote,
    updateNote,
    deleteNote,
)

urlpatterns = [
    # URl pattern for displaying a list of all sticky notes
    path("", viewAll, name="viewAll"),

    # URL pattern for displaying the detail of a selected sticky note
    path("note/<int:pk>/", note_detail, name="note_detail"),

    # URL pattern for creating a new sticky note
    path("note/new/", createNote, name="createNote"),

    # URL pattern for updating an existing sticky note
    path("note/<int:pk>/edit/", updateNote, name="updateNote"),

    # URL pattern for deleting an existing sticky note
    path("note/<int:pk>/delete/", deleteNote, name="deleteNote"),
]
