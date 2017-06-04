from django.contrib import admin
from .models import Person, Contract, Title, Book, File, Transaction, Currency


@admin.register(Person, Contract, Title, Book, File, Transaction, Currency)
class AerariumAdmin(admin.ModelAdmin):
    readonly_fields = ('created_timestamp', 'updated_timestamp')
