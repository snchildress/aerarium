from django.contrib import admin
from .models import Person, Contract, Title, Book


@admin.register(Person, Contract, Title, Book)
class AerariumAdmin(admin.ModelAdmin):
    readonly_fields = ('created_timestamp', 'updated_timestamp')
