from django.core.exceptions import ValidationError
from rest_framework import serializers
from .models import *


class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = ('id', 'title', 'subtitle', 'context', 'author', 'isbn', 'price')

    def validate(self, data):
        title = data.get('title', None)
        author = data.get('author', None)
        if not title.isalpha():
            raise ValidationError({
                "status": False,
                "message": "Iltimos suz kiriting "
                }
            )

        if Book.objects.filter(title=title, author=author).exists():
            raise ValidationError({
                "status": False,
                "message": "Sarlavha va muallif bir xil bulmasligi kerak"
                }
            )

        return data
