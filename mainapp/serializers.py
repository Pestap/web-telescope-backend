from rest_framework import serializers
from mainapp.models import *


class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = ['id', 'title', 'alt', 'url']


class PhotoSmallSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = ['api_url']


class ParagraphSerializer(serializers.ModelSerializer):
    photos = PhotoSmallSerializer(many=True, allow_null=True)

    class Meta:
        model = Paragraph
        fields = ['id', 'title', 'text', 'photos']


class ParagraphSmallSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paragraph
        fields = ['api_url']


class TopicSerializer(serializers.ModelSerializer):
    photos = PhotoSmallSerializer(many=True, allow_null=True)
    paragraphs = ParagraphSmallSerializer(many=True)

    class Meta:
        model = Topic
        fields = ['id', 'title', 'visits', 'time_investment', 'edit_date', 'difficulty', 'paragraphs', 'photos']


class TopicSmallSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = ['api_url']


class ChapterSerializer(serializers.ModelSerializer):
    photos = PhotoSmallSerializer(many=True, allow_null=True)
    topics = TopicSmallSerializer(many=True)

    class Meta:
        model = Chapter
        fields = ['id', 'title', 'summary', 'time_investment', 'topics', 'photos']


class ChapterSmallSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chapter
        fields = ['api_url']


class SectionSerializer(serializers.ModelSerializer):

    chapters = ChapterSmallSerializer(many=True, allow_null=True)

    class Meta:
        model = Section
        fields = ['id', 'title', 'summary', 'time_investment', 'photo', 'chapters']

### 'TESTS' in application


class AnswerSerializerNoResult(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ['id', 'text', 'photo', 'api_url_check']


class AnswerSerializerWithResult(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ['id', 'text', 'photo', 'is_correct']


class AnswerSmallSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ['api_url']


class QuestionSerializer(serializers.ModelSerializer):
    answers = AnswerSmallSerializer(many=True)
    class Meta:
        model = Question
        fields = ['id', 'question', 'photo', 'answers']


class QuestionSmallSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['api_url']


class TestSerializer(serializers.ModelSerializer):
    questions = QuestionSmallSerializer(many=True)

    class Meta:
        model = Test
        fields = ['id', 'title', 'number_of_questions', 'questions']


