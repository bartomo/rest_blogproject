from rest_framework import serializers
from .models import Entry, User

class EntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Entry
        fields = ('id','title','content','category','user_name')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('user_name', 'authorname', 'mail')