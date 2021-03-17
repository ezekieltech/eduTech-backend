from django.contrib import admin
from .models import Author, Genre, Book, BookInstance


admin.site.register(Genre)


# Define the admin class

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')

    # Detail view: Controlling which fields are displayed and laid out
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]

class BooksInstanceInline(admin.TabularInline):
    model = BookInstance

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    # list_display = ('title', 'author', 'genre')
    # todo The value of 'list_display[2]' must not be a ManyToManyField.
    list_display = ('title', 'author')

    # Display: Inline editing of associated records
    inlines = [BooksInstanceInline]


@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('book', 'status', 'borrower', 'due_back', 'id')
    list_filter = ('status', 'due_back')

    # Detail view: sectioning the admin section
    fieldsets = (
        (None, {
            'fields': ('book', 'imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back', 'borrower')
        }),
    )