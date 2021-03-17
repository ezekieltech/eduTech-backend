from rest_framework import serializers
from catalogue.models import Book, Author, BookInstance


class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = '__all__'


class AuthorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Author
        fields = '__all__'

# class RenewBookFormSerializer(serializers.Serializer):
#     date = serializers.DateField()

#     def create(self, validated_data):
#         return RenewBookForm(**validated_data)

#     def update(self, instance, validated_data):
#         """
#         Update and return an existing `Snippet` instance, given the validated data.
#         """
#         instance.date = validated_data.get('date', instance.date)
#         instance.save()
#         return instance

class RenewBookFormSerializer(serializers.ModelSerializer):

    class Meta:
        model = BookInstance
        fields = ['id','book', 'status','borrower','due_back', 'is_overdue']