from django.test import TestCase
from story8.models import Book

# Create your tests here.
class story8ModelsTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.test_book = Book.objects.create(
            bookName = 'The Intelligent Investor'
        ) 
    
    def test_bookName(self):
        book_name = Book.objects.get(id = 1)
        field_label = book_name.bookName
        expected_book_name = f'{book_name.bookName}'
        self.assertEqual(field_label, 'The Intelligent Investor')
        self.assertEqual(expected_book_name, str(book_name))
    