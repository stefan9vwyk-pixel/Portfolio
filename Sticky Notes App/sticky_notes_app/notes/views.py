from django.shortcuts import render, get_object_or_404, redirect
from .models import Note
from .forms import NoteForm


def viewAll(request):
    """
    View to display a list of all sticky notes

    :param request: HTTP request object.
    :return: Rendered template with a list of sticky notes
    """
    notes = Note.objects.all()

    context = {
        "notes": notes,
        "page_title": "List of Sticky Notes",
    }

    return render(request, "notes/viewAll.html", context)


def note_detail(request, pk):
    """
    View to display details of a sticky note
    :param:
        request: HTTP request object.
        pk: Primary key of the sticky note.
    :return: Rendered template with details of the selected post.
    """
    note = get_object_or_404(Note, pk=pk)
    return render(request, "notes/note_detail.html", {"note": note})


def createNote(request):
    """
    View to create a new sticky note.

    :param: HTTP request object.
    :return: Rendered template for creating a new sticky note.
    """

    if request.method == "POST":
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.save()
            return redirect("viewAll")
        else:
            print(form.errors)
    else:
        form = NoteForm()

    return render(request, "notes/note_form.html", {"form": form})


def updateNote(request, pk):
    """
    View to update an existing sticky note.

    :param:
        request: HTTP request object.
        pk: Primary key for the sticky note to be updated.
    :return: Rendered template for updating the selected sticky note.
    """

    note = get_object_or_404(Note, pk=pk)

    if request.method == "POST":
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            note = form.save(commit=False)
            note.save()
            return redirect("viewAll")

    else:
        form = NoteForm(instance=note)

    return render(request, "notes/note_form.html", {"form": form})


def deleteNote(request, pk):
    """
    View to delete an existing sticky note.

    :param:
        request: HTTP request object.
        pk: Primary key of the sticky note to be deleted.
    return: Redirect to the sticky notes list after deletion.
    """

    note = get_object_or_404(Note, pk=pk)
    note.delete()
    return redirect("viewAll")
