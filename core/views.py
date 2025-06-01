from django.http import JsonResponse
from .models import Book
import threading

def create_book(request):
    print("Thread ID (view):", threading.get_ident())
    
    book = Book(title="Django Signals")
    book.save()
    
    return JsonResponse({"message": "Book created"})
