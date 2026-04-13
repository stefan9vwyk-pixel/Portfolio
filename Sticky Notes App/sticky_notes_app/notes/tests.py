from django.test import TestCase, RequestFactory
from django.urls import reverse
from .models import Note
from .views import deleteNote


class NoteModelTest(TestCase):
    def setUp(self):
        """Create a Note object for testing"""
        Note.objects.create(title='Test Note',
                            content='This is a sticky note test.')

    def test_note_has_title(self):
        """Test that Note object has expected title"""
        note = Note.objects.get(id=1)
        self.assertEqual(note.title, 'Test Note')

    def test_note_has_content(self):
        """Test that Note object has expected content"""
        note = Note.objects.get(id=1)
        self.assertEqual(note.content, 'This is a sticky note test.')


class NoteViewTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        """Create a Note object for testing"""
        self.note = Note.objects.create(title='Test Note',
                                        content='This is a sticky note test.')

    def test_viewAll_view(self):
        """Test the viewAll view"""
        response = self.client.get(reverse('viewAll'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Note')

    def test_deleteNote_view(self):
        """Test the deleteNote view"""
        # Setup the request for the primary key (pk)
        url = reverse('deleteNote', kwargs={'pk': self.note.pk})
        request = self.factory.post(url)

        # Call the view
        response = deleteNote(request, pk=self.note.pk)

        # Check for the redirect
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse('viewAll'))

        # Verify the note is actually deleted from the database
        self.assertFalse(Note.objects.filter(pk=self.note.pk).exists())
