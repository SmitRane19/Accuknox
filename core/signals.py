import threading
import time
from django.db import transaction
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Book

@receiver(post_save, sender=Book)
def book_saved(sender, instance, **kwargs):
    print("🚨 Signal triggered")
    print("Thread ID (signal):", threading.get_ident())
    
    # Artificial delay
    time.sleep(5)

    # Check if in transaction
    if transaction.get_connection().in_atomic_block:
        print("✅ Signal is inside DB transaction")
    else:
        print("❌ Signal is outside DB transaction")
