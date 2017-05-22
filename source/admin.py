from django.contrib import admin
from .models import Person, Contract, Title, Book


@admin.register(Person, Contract, Title, Book)
class AerariumAdmin(admin.ModelAdmin):
    pass
