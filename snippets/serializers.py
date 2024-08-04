from rest_framework import serializers
from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES
from django.contrib.auth.models import User
from rest_framework import permissions


class UserSerializer(serializers.ModelSerializer):
    snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=Snippet.objects.all())

    #permisions that allow only authenticated users to get read, write accesses while the lest get only r5ead access
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


    class Meta:
        model = User
        fields = ['id', 'username', 'snippet']
class SnippetSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    class Meta:
        model = Snippet
        fields = ['id', 'title', 'code', 'linenos', 'language', 'style', 'owner']