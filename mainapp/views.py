from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from mainapp.serializers import *
from mainapp.models import *
# Create your views here.


class PhotoDetailView(APIView):
    """
    A view to fetch Photo objects based on id
    """
    @staticmethod
    def get_object(photo_id):
        """
        Return an object instance or None if id is invalid
        """
        try:
            return Photo.objects.get(id=photo_id)
        except Photo.DoesNotExist:
            return None

    def get(self, request, photo_id, *args, **kwargs):
        """
        GET method for Photo objects
        """
        photo = self.get_object(photo_id)
        if not photo:
            # Handle the case when id is not valid
            return Response({"Reason": "Photo with a provided id does not exist"}, status=status.HTTP_404_NOT_FOUND)

        serializer = PhotoSerializer(photo)
        # Return a serialized photo object
        return Response(serializer.data, status=status.HTTP_200_OK)


class SectionView(APIView):
    """
    A view to fetch all objects from SECTIONS table
    """
    def get(self, request, *args, **kwargs):
        """
        GET method handling, it fetches all Section objects
        """
        sections = Section.objects.all()
        serializer = SectionSerializer(sections, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class SectionDetailView(APIView):
    """
    A view for fetching one section, specified by section id
    """
    @staticmethod
    def get_object(section_id):
        """
        A method for fetching a single object by id
        """
        try:
            return Section.objects.get(id=section_id)
        except Section.DoesNotExist:
            return None

    def get(self, request, section_id, *args, **kwargs):
        """
        GET method for fetching one Section object by section_id
        """
        section = self.get_object(section_id)
        if not section:
            # Handle the case when there is no section with a given id
            return Response({"Reason": "Section with a provided id does not exist"}, status=status.HTTP_404_NOT_FOUND)

        serializer = SectionSerializer(section)
        # Serialize the object and return a response
        return Response(serializer.data, status=status.HTTP_200_OK)


class ChapterDetailView(APIView):
    """
    A view for fetching chapters
    """
    @staticmethod
    def get_object(chapter_id):
        """
        Return an object instance or None if id is invalid
        """
        try:
            return Chapter.objects.get(id=chapter_id)
        except Chapter.DoesNotExist:
            return None

    def get(self, request, chapter_id, *args, **kwargs):
        """
        GET method for fetching a Chapter object by id
        """
        chapter = self.get_object(chapter_id)
        if not chapter:
            # Handle case when id is invalid
            return Response({"Reason" : "Chapter with a provided id does not exist"}, status=status.HTTP_404_NOT_FOUND)

        serializer = ChapterSerializer(chapter)
        # Serialize the Chapter and return
        return Response(serializer.data, status=status.HTTP_200_OK)


class TopicDetailView(APIView):
    """
    A view for fetching Topic objects
    """
    @staticmethod
    def get_object(topic_id):
        """
        A method to fetch a single object
        """
        try:
            return Topic.objects.get(id=topic_id)
        except Topic.DoesNotExist:
            return None

    def get(self, request, topic_id, *args, **kwargs):
        """
        GET method for Topic fetching
        """
        topic = self.get_object(topic_id)

        if not topic:
            # Handle the case when id invalid
            return Response({"Reason": "Topic with a provided id does not exist"}, status=status.HTTP_404_NOT_FOUND)

        # Update topic visit count
        topic.visits = topic.visits + 1
        topic.save()
        # Serialize the topic and return response
        serializer = TopicSerializer(topic)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ParagraphDetailView(APIView):
    """
    A view for fetching Paragraph objects
    """
    @staticmethod
    def get_object(paragraph_id):
        """
        A method for fetching a single Paragraph by id
        """
        try:
            return Paragraph.objects.get(id=paragraph_id)
        except Paragraph.DoesNotExist:
            return None

    def get(self, request, paragraph_id, *args, **kwargs):
        """
        GET method for fetching Paragraph objects by id
        """
        paragraph = self.get_object(paragraph_id)
        if not paragraph:
            # Handle invalid id
            return Response({"Reason": "Paragraph with a provided id does not exist"}, status=status.HTTP_404_NOT_FOUND)

        # Serialize and return the desired object
        serializer = ParagraphSerializer(paragraph)
        return Response(serializer.data, status=status.HTTP_200_OK)


class AnswerDetailViewNoResult(APIView):
    """
    A view for fetching Answer objects - no result
    """
    @staticmethod
    def get_object(answer_id):
        """
        method for fetching an answer object
        """
        try:
            return Answer.objects.get(id=answer_id)
        except Answer.DoesNotExist:
            return None

    def get(self, request, answer_id, *args, **kwargs):
        """
        GET method for fetching Answer objects
        """
        answer = self.get_object(answer_id)
        if not answer:
            # Handle invalid id
            return Response({"Reason": "Answer with a provided id does not exist"}, status=status.HTTP_404_NOT_FOUND)

        # serialize the result and return
        serializer = AnswerSerializerNoResult(answer)
        return Response(serializer.data, status=status.HTTP_200_OK)


class AnswerDetailViewResult(APIView):
    """
    A view for fetching Answer objects - with results
    """
    @staticmethod
    def get_object(answer_id):
        """
        A method for fetching a single Answer
        """
        try:
            return Answer.objects.get(id=answer_id)
        except Answer.DoesNotExist:
            return None

    def get(self, request, answer_id, *args, **kwargs):
        """
        GET method for fetching Answer objects
        """
        answer = self.get_object(answer_id)
        if not answer:
            # Handle invalid id
            return Response({"Reason": "Answer with a provided id does not exist"}, status=status.HTTP_404_NOT_FOUND)

        # Serialize and return the result
        serializer = AnswerSerializerWithResult(answer)
        return Response(serializer.data, status=status.HTTP_200_OK)


class QuestionDetailView(APIView):
    """
    A view for fetching Question objects
    """
    @staticmethod
    def get_object(question_id):
        """
        A method for fetching a single Question object
        """
        try:
            return Question.objects.get(id=question_id)
        except Question.DoesNotExist:
            return None

    def get(self, request, question_id, *args, **kwargs):
        """
        GET method for fetching Questions objects
        """
        question = self.get_object(question_id)
        if not question:
            # Handle invalid id
            return Response({"Reason": "Question with a provided id does not exist"}, status=status.HTTP_404_NOT_FOUND)

        # Serialize and return the result
        serializer = QuestionSerializer(question)
        return Response(serializer.data, status=status.HTTP_200_OK)


class TestDetailView(APIView):
    """
    A view for fetching Test objecst
    """
    @staticmethod
    def get_object(test_id):
        """
        A method for fetchin a single Test object
        """
        try:
            return Test.objects.get(id=test_id)
        except Test.DoesNotExist:
            return None

    def get(self, request, test_id, *args, **kwargs):
        """
        GET method for fetching Test objects
        """
        test = self.get_object(test_id)
        if not test:
            # Handle invalid id
            return Response({"Reason": "Test with a provided id does not exist"}, status=status.HTTP_404_NOT_FOUND)

        # Serialize and return thr result
        serializer = TestSerializer(test)
        return Response(serializer.data, status=status.HTTP_200_OK)


class UserDetailView(APIView):
    """
    A view for creating users - User + UserProfile - same PK (id)
    """
    @staticmethod
    def get_object(user_id):
        """
        A method for fetching a UserProfile
        """
        try:
            return UserProfile.objects.get(id=user_id)
        except UserProfile.DoesNotExist:
            return None

    def get(self, request, user_id, *args, **kwargs):
        """
        GET method for UserProfile objects
        """
        user = self.get_object(user_id)
        if not user:
            # Handle invalid id
            return Response({"Reason": "User with a provided id does not exist"}, status=status.HTTP_404_NOT_FOUND)

        # Serialize and return the result
        serializer = UserProfileSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        """
        POST method for creating User and UserProfile
        """

        # Create user based on the data provided in the request
        serializer_user = UserSerializer(data=request.data)
        # Check if data is valid
        if serializer_user.is_valid():
            # Create the User
            serializer_user.save()
            # Fetch the user from database
            user = User.objects.get(username=request.data.get('username'))
            request.data['id'] = user.id # change the id to the one autogenerated by DB
            request.data['user'] = user.id

            serializer_user_profile = UserProfileSerializerForPost(data=request.data)
            if serializer_user_profile.is_valid():
                # If data is valid, save the UserProfile and return it
                serializer_user_profile.save()
                return Response(request.data, status=status.HTTP_201_CREATED)

            # If data was invalid delete the user
            user.delete()
            return Response(serializer_user_profile.errors, status.HTTP_400_BAD_REQUEST)

        # If invalid return bad request
        return Response(serializer_user.errors, status.HTTP_400_BAD_REQUEST)


class UserCompletedTopicsView(APIView):
    """
    View for fetching user's completed topics
    """
    def get(self, request, user_id, *args, **kwargs):
        """
        GET method for fetching topics completed by the user
        """
        user = UserProfile.objects.get(id=user_id)
        if not user:
            # If invalid id
            return Response({"Reason": "User with provided id does not exist"}, status=status.HTTP_400_BAD_REQUEST)

        # Fetch topics that have been completed by the user
        topics = Topic.objects.filter(completed_topics__in=user.completed_topics.all())

        # Serialize and return the result
        serializer = TopicSmallSerializer(topics, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, user_id, *args, **kwargs):
        """
        POST method for marking topics as completed
        """
        # Get the user and topic
        user = UserProfile.objects.get(id=user_id)
        topic = Topic.objects.get(id=request.data.get('topic_id'))

        # Check if both exist
        if not user or not topic:
            return Response({"Reason": "Topic or user id does not exist"}, status=status.HTTP_400_BAD_REQUEST)

        # Check if topic already completed by user
        if CompletedTopic.objects.filter(user=user_id, topic=topic.id).exists():
            return Response({"Reason": "That user already completed that topic"}, status=status.HTTP_400_BAD_REQUEST)


        # Create CompletedTopic object
        completed_topic = CompletedTopic.objects.create()
        completed_topic.user = user
        completed_topic.topic = topic
        completed_topic.save()

        # TODO: xp adding based on topic difficulty ( x 0.5, 1.0, 1.5 ) and level handling

        # Add completed topic to user

        return Response(status=status.HTTP_200_OK)

    def delete(self, request, user_id, topic_id, *args, **kwargs):
        """
        DELETE method for deleting CampletedTopics
        """
        # Get both user and topic
        user = UserProfile.objects.get(id=user_id)
        topic = Topic.objects.get(id=topic_id)

        if not user or not topic:
            return Response({"Reason": "Topic or user with provided id does not exist"}, status=status.HTTP_400_BAD_REQUEST)


        if not CompletedTopic.objects.filter(user=user_id, topic=topic.id).exists():
            return Response({"Reason": "That user has NOT completed that topic"}, status=status.HTTP_400_BAD_REQUEST)

        completed_topic = CompletedTopic.objects.get(user=user_id, topic=topic_id)
        completed_topic.delete()


        return Response({"Result": "Topic is no longer marked as completed"}, status=status.HTTP_200_OK)


class UserFavouritedTopicsView(APIView):
    """
    View for fetching user's favourited topics
    """
    def get(self, request, user_id, *args, **kwargs):
        """
        GET method for fetching topics favourited by the user
        """
        # Fetch user
        user = UserProfile.objects.get(id=user_id)
        if not user:
            # If invalid id
            return Response({"Reason": "User with provided id does not exist"}, status=status.HTTP_400_BAD_REQUEST)

        # Fetch topics that have been marked as favourite by the user
        topics = Topic.objects.filter(favourited_topics__in=user.favourited_topics.all())

        # Serialize and return the result
        serializer = TopicSmallSerializer(topics, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, user_id, *args, **kwargs):
        """
        POST method for marking topics as favourited
        """
        # Get the user and topic
        user = UserProfile.objects.get(id=user_id)
        topic = Topic.objects.get(id=request.data.get('topic_id'))

        # Check if both exist
        if not user or not topic:
            return Response({"Reason": "Topic or user id does not exist"}, status=status.HTTP_400_BAD_REQUEST)

        # Check if topic already completed by user
        if FavouritedTopic.objects.filter(user=user_id, topic=topic.id).exists():
            return Response({"Reason": "That user already marked that topic as favourite"}, status=status.HTTP_400_BAD_REQUEST)

        # Create Favourited object object
        favourited_topic = FavouritedTopic.objects.create()
        favourited_topic.user = user
        favourited_topic.topic = topic
        favourited_topic.save()

        return Response(status=status.HTTP_200_OK)

    def delete(self, request, user_id, topic_id, *args, **kwargs):
        """
        DELETE method for unfavouriting Topics
        """
        user = UserProfile.objects.get(id=user_id)
        topic = Topic.objects.get(id=topic_id)

        if not user or not topic:
            return Response({"Reason": "Topic or user with provided id does not exist"}, status=status.HTTP_400_BAD_REQUEST)



        if not FavouritedTopic.objects.filter(user=user, topic=topic).exists():
            return Response({"Reason": "User has not marked that topic as favourite"}, status=status.HTTP_400_BAD_REQUEST)

        favourited_topic = FavouritedTopic.objects.get(user=user, topic=topic)
        favourited_topic.delete()

        return Response({"Result": "Topic in no longer marked as favourite"}, status=status.HTTP_200_OK)

class UserScoreView(APIView):
    def get(self, request, user_id, *args, **kwargs):
        scores = Score.objects.filter(user=user_id)
        serializer = ScoreSerializer(scores, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, user_id, *args, **kwargs):
        # Get user
        user = User.objects.get(id=user_id)
        # Get test
        test = Test.objects.get(id=request.data.get('test'))
        if not user or not test:
            return Response({"res": "Invalid data"}, status=status.HTTP_400_BAD_REQUEST)
        data = {
            'score': request.data.get('score'),
            'date': request.data.get('date'),
            'user': user.id,
            'test': test.id
        }

        serializer = ScoreSerializerForPost(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




