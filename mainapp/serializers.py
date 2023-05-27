from rest_framework import serializers
from mainapp.models import *


# EDUCATIONAL PART OF THE APPLICATION
class PhotoSerializer(serializers.ModelSerializer):
    """
    A serializer to use when fetching Photo objects
    """
    class Meta:
        model = Photo
        fields = ['id', 'title', 'alt', 'url']


class PhotoSmallSerializer(serializers.ModelSerializer):
    """
    A serializer to use when representing photo objects in different models serializations
    """
    class Meta:
        model = Photo
        fields = ['api_url']


class ParagraphSerializer(serializers.ModelSerializer):
    """
    Paragraph serializer to user when fetching Paragraph objects
    """
    photos = PhotoSerializer(many=True, allow_null=True)
    # get photos of the paragraph (small representation)

    class Meta:
        model = Paragraph
        fields = ['id', 'title', 'text', 'photos']


class ParagraphSmallSerializer(serializers.ModelSerializer):
    """
    Paragraph serializer for use in different models - small representation
    """
    class Meta:
        model = Paragraph
        fields = ['api_url', 'id', 'title'] # TODO: maybe add id and title


class TopicSerializer(serializers.ModelSerializer):
    """
    Topic serializer to use when fetching Topic objects
    """
    photos = PhotoSerializer(many=True, allow_null=True) # photos in small representation
    paragraphs = ParagraphSerializer(many=True) # paragraphs in small representation

    class Meta:
        model = Topic
        fields = ['id', 'title', 'visits', 'time_investment', 'edit_date', 'difficulty', 'paragraphs', 'photos']


class TopicSmallSerializer(serializers.ModelSerializer):
    """
    Topic serializer for use in other objects - small representation
    """
    class Meta:
        model = Topic
        fields = ['api_url', 'id', 'title']


class ChapterSerializer(serializers.ModelSerializer):
    """
    Chapter serializer for use when fetching chapter objects
    """
    photos = PhotoSerializer(many=True, allow_null=True) # photos in small representation
    topics = TopicSmallSerializer(many=True) # topics in small representation

    class Meta:
        model = Chapter
        fields = ['id', 'title', 'summary', 'time_investment', 'topics', 'photos']


class ChapterSmallSerializer(serializers.ModelSerializer):
    """
    A small chapter serializer for use in different objects
    """
    class Meta:
        model = Chapter
        fields = ['api_url', 'id', 'title'] # TODO: maybe add id and title


class SectionSerializer(serializers.ModelSerializer):
    """
    A section serializer for use when fetching Section objects
    """
    chapters = ChapterSerializer(many=True, allow_null=True) # section's chapters in small representation
    photo = PhotoSerializer(allow_null=True)
    class Meta:
        model = Section
        fields = ['id', 'title', 'summary', 'time_investment', 'photo', 'chapters']


# TESTING PART OF THE APPLICATION
class AnswerSerializerNoResult(serializers.ModelSerializer):
    """
    A serializer for answer without the result (has a url for check)
    """
    class Meta:
        model = Answer
        fields = ['id', 'text', 'photo', 'api_url_check']


class AnswerSerializerWithResult(serializers.ModelSerializer):
    """
    Answer serializer with result
    """
    photo = PhotoSerializer()
    class Meta:
        model = Answer
        fields = ['id', 'text', 'photo', 'is_correct']


class AnswerSmallSerializer(serializers.ModelSerializer):
    """
    Answer small serializer for use in other objects
    """
    class Meta:
        model = Answer
        fields = ['api_url']


class QuestionSerializer(serializers.ModelSerializer):
    """
    Question serializer for use when fetching questions
    """
    answers = AnswerSerializerNoResult(many=True) # answers in small representaion
    photo = PhotoSerializer()

    class Meta:
        model = Question
        fields = ['id', 'question', 'photo', 'answers']


class QuestionSmallSerializer(serializers.ModelSerializer):
    """
    A small question serializer for use in other objects
    """
    class Meta:
        model = Question
        fields = ['api_url']


class TestSerializer(serializers.ModelSerializer):
    """
    Test serializer for use when fetching Test objects
    """
    questions = QuestionSerializer(many=True) # questions in small representation

    class Meta:
        model = Test
        fields = ['id', 'title', 'number_of_questions', 'questions']


class TestSmallSerializer(serializers.ModelSerializer):
    """
    A small Test serializer for use in other objects
    """
    class Meta:
        model = Test
        fields = ['id', 'title', 'number_of_questions', 'api_url']


class UserProfileSerializer(serializers.ModelSerializer):
    """
    A serializer to use when fetching UserProfile objects
    """

    class Meta:
        model = UserProfile
        fields = ['id', 'role', 'email', 'level', 'xp', 'username']


class UserProfileSerializerForPost(serializers.ModelSerializer):
    """
    A seriailizer to use when information about the User is needed
    """
    class Meta:
        model = UserProfile
        fields = ['id', 'role', 'email', 'level', 'xp', 'user']


class UserProfileCompletedTopicSerializer(serializers.ModelSerializer):
    """
    A serializer to use when fetching user with completed topics
    """
    completed_topics = TopicSmallSerializer(many=True) # completed_topics small representation

    class Meta:
        model = UserProfile
        fields = ['id', 'role', 'email', 'level', 'xp', 'completed_topics']


class UserProfileFavouritedTopicSerializer(serializers.ModelSerializer):
    """
    A serializer to use when fetching user's favourited topics
    """
    favourited_topics = TopicSmallSerializer(many=True) # favourired topics small represenation

    class Meta:
        model = UserProfile
        fields = ['id', 'role', 'email', 'level', 'xp', 'favourited_topics']


class ScoreSerializer(serializers.ModelSerializer):
    """
    Score serializer when fetchin scores
    """
    test = TestSmallSerializer()

    class Meta:
        model = Score
        fields = ['score', 'date', 'user', 'test']


class ScoreSerializerForPost(serializers.ModelSerializer):
    """
    Score serializer for posting scores - test id instead of a whole test object
    """
    class Meta:
        model = Score
        fields = ['score', 'date', 'user', 'test']


class UserSerializer(serializers.ModelSerializer):
    """
    User serializer used for creating users
    """
    class Meta:
        model = User
        fields = ('username', 'password', 'email')
        write_only_fields = ('password',)


