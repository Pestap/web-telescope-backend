from rest_framework import serializers
from mainapp.models import *




class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = ['id', 'title', 'alt', 'url']

class PhotoSmallSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = ['id']


class ParagraphSerializer(serializers.ModelSerializer):
    photos = PhotoSmallSerializer(many=True, allow_null=True)

    class Meta:
        model = Paragraph
        fields = ['id', 'title', 'text', 'photos']


class ParagraphSmallSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paragraph
        fields = ['id']
class TopicSerializer(serializers.ModelSerializer):
    photos = PhotoSmallSerializer(many=True, allow_null=True)
    paragraphs = ParagraphSmallSerializer(many=True)

    class Meta:
        model = Topic
        fields = ['id', 'title', 'visits', 'time_investment', 'edit_date', 'difficulty', 'paragraphs', 'photos']


class TopicSmallSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = ['id']


class ChapterSerializer(serializers.ModelSerializer):
    photos = PhotoSmallSerializer(many=True, allow_null=True)
    topics = TopicSmallSerializer(many=True)
    class Meta:
        model = Chapter
        fields = ['id', 'title', 'summary', 'time_investment', 'topics', 'photos']


class ChapterSmallSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chapter
        fields = ['id']


class SectionSerializer(serializers.ModelSerializer):

    chapters = ChapterSmallSerializer(many=True, allow_null=True)

    class Meta:
        model = Section
        fields = ['id', 'title', 'summary', 'time_investment', 'photo', 'chapters']




