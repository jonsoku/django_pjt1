from rest_framework import serializers
from .models import Notice

class NoticeSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'title', 'content', 'view_count', 'created_date', 'published_date', 'author')
        model = Notice
        
