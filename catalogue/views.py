from django.shortcuts import render
from django.views import generic

from rest_framework import status, viewsets
from rest_framework.response import Response

from .models import Book, Author, BookInstance
from .serializers import BookSerializer, AuthorSerializer, RenewBookFormSerializer
# Create your views here.


class BookViewset(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    # todo paginate_by = 10, frontend or backend


class AuthorViewset(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class BookInstanceViewSet(viewsets.ModelViewSet):
    queryset = BookInstance.objects.all()
    serializer_class = RenewBookFormSerializer

# import datetime

# from django.shortcuts import render, get_object_or_404
# from django.http import HttpResponseRedirect
# from django.urls import reverse
# from rest_framework.decorators import api_view
# from rest_framework import serializers 

# from catalogue.forms import RenewBookForm

# @api_view(['GET', 'POST'])
# def renew_book_librarian(request, pk):
#     book_instance = get_object_or_404(BookInstance, pk=pk)

#     # If this is a POST request then process the Form data
#     if request.method == 'POST':

#         # Create a form instance and populate it with data from the request (binding):
#         form = RenewBookForm(request.POST)

#         # Check if the form is valid:
#         if form.is_valid():
#             # process the data in form.cleaned_data as required (here we just write it to the model due_back field)
#             book_instance.due_back = form.cleaned_data['renewal_date']
#             book_instance.save()

#             # redirect to a new URL:
#             reversed_url = reverse('all-borrowed')
#             return {"reversed_url": reversed_url}

#     # If this is a GET (or any other method) create the default form.
#     else:
#         proposed_renewal_date = datetime.date.today() + datetime.timedelta(weeks=3)
#         form = RenewBookForm(initial={'renewal_date': proposed_renewal_date})

#     context = {
#         'form': form,
#         'book_instance': book_instance,
#     }

#     print(context)

#     context = RenewBookFormSerializer(context)

#     return Response(context.data, status=status.HTTP_202_ACCEPTED)