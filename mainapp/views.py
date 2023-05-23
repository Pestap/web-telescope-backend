from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from mainapp.serializers import *
from mainapp.models import *
# Create your views here.


class SectionView(APIView):
    def get(self, request, *args, **kwargs):
        sections = Section.objects.all()
        serializer = SectionSerializer(sections, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class PhotoApiView(APIView):
    def get(self, request, *args, **kwargs):
        photos = Photo.objects.all()
        serializer = PhotoSerializer(photos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class PhotoDetailApiView(APIView):

    def get_object(self, photo_id):
        try:
            return Photo.objects.get(id=photo_id)
        except Photo.DoesNotExist:
            return None

    def get(self, request, photo_id, *args, **kwargs):
        photo = self.get_object(photo_id)
        if not photo:
            return Response({"res": "Photo with a provided id does not exist"}, status=status.HTTP_404_NOT_FOUND)

        serializer = PhotoSerializer(photo)
        return Response(serializer.data, status=status.HTTP_200_OK)


class SectionDetailView(APIView):

    def get_object(self, section_id):
        try:
            return Section.objects.get(id=section_id)
        except Section.DoesNotExist:
            return None

    def get(self, request, section_id, *args, **kwargs):
        section = self.get_object(section_id)
        if not section:
            return Response({"res" : "Section with a provided id does not exist"}, status=status.HTTP_404_NOT_FOUND)

        serializer = SectionSerializer(section)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ChapterDetailView(APIView):

    def get_object(self, chapter_id):
        try:
            return Chapter.objects.get(id=chapter_id)
        except Chapter.DoesNotExist:
            return None

    def get(self, request, chapter_id, *args, **kwargs):
        chapter = self.get_object(chapter_id)
        if not chapter:
            return Response({"res" : "Chapter with a provided id does not exist"}, status=status.HTTP_404_NOT_FOUND)

        serializer = ChapterSerializer(chapter)
        return Response(serializer.data, status=status.HTTP_200_OK)


class TopicDetailView(APIView):

    def get_object(self, topic_id):
        try:
            return Topic.objects.get(id=topic_id)
        except Topic.DoesNotExist:
            return None

    def get(self, request, topic_id, *args, **kwargs):
        topic = self.get_object(topic_id)

        if not topic:
            return Response({"res" : "topic with a provided id does not exist"}, status=status.HTTP_404_NOT_FOUND)

        topic.visits = topic.visits + 1
        topic.save()
        serializer = TopicSerializer(topic)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ParagraphDetailView(APIView):
    def get_object(self, paragraph_id):
        try:
            return Paragraph.objects.get(id=paragraph_id)
        except Paragraph.DoesNotExist:
            return None

    def get(self, request, paragraph_id, *args, **kwargs):
        paragraph = self.get_object(paragraph_id)
        if not paragraph:
            return Response({"res" : "Paragraph with a provided id does not exist"}, status=status.HTTP_404_NOT_FOUND)

        serializer = ParagraphSerializer(paragraph)
        return Response(serializer.data, status=status.HTTP_200_OK)


class AnswerDetailViewNoResult(APIView):
    def get_object(self, answer_id):
        try:
            return Answer.objects.get(id=answer_id)
        except Answer.DoesNotExist:
            return None

    def get(self, request, answer_id, *args, **kwargs):
        answer = self.get_object(answer_id)
        if not answer:
            return Response({"res" : "Answer with a provided id does not exist"}, status=status.HTTP_404_NOT_FOUND)

        serializer = AnswerSerializerNoResult(answer)
        return Response(serializer.data, status=status.HTTP_200_OK)


class AnswerDetailViewResult(APIView):
    def get_object(self, answer_id):
        try:
            return Answer.objects.get(id=answer_id)
        except Answer.DoesNotExist:
            return None

    def get(self, request, answer_id, *args, **kwargs):
        answer = self.get_object(answer_id)
        if not answer:
            return Response({"res" : "Answer with a provided id does not exist"}, status=status.HTTP_404_NOT_FOUND)

        serializer = AnswerSerializerWithResult(answer)
        return Response(serializer.data, status=status.HTTP_200_OK)


class QuestionDetailView(APIView):
    def get_object(self, question_id):
        try:
            return Question.objects.get(id=question_id)
        except Question.DoesNotExist:
            return None

    def get(self, request, question_id, *args, **kwargs):
        question = self.get_object(question_id)
        if not question:
            return Response({"res" : "Question with a provided id does not exist"}, status=status.HTTP_404_NOT_FOUND)

        serializer = QuestionSerializer(question)
        return Response(serializer.data, status=status.HTTP_200_OK)


class TestDetailView(APIView):
    def get_object(self, test_id):
        try:
            return Test.objects.get(id=test_id)
        except Test.DoesNotExist:
            return None

    def get(self, request, test_id, *args, **kwargs):
        test = self.get_object(test_id)
        if not test:
            return Response({"res" : "Test with a provided id does not exist"}, status=status.HTTP_404_NOT_FOUND)

        serializer = TestSerializer(test)
        return Response(serializer.data, status=status.HTTP_200_OK)


class UserView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserDetailView(APIView):
    def get_object(self, user_id):
        try:
            return UserProfile.objects.get(id=user_id)
        except UserProfile.DoesNotExist:
            return None

    def get(self, request, user_id, *args, **kwargs):
        user = self.get_object(user_id)
        if not user:
            return Response({"res" : "User with a provided id does not exist"}, status=status.HTTP_404_NOT_FOUND)

        serializer = UserProfileSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)


    def post(self, request, *args, **kwargs):

        serializer_user = UserSerializer(data=request.data)
        if serializer_user.is_valid():
            serializer_user.save()
            # pobieramy usera
            user = User.objects.get(username=request.data.get('username'))
            request.data['id'] = user.id # przypisujemy id usera do id
            request.data['user'] = user.id  # przypisujemy id usera do id
            serializer_user_profile = UserProfileSerializerForPost(data=request.data)
            if serializer_user_profile.is_valid():
                serializer_user_profile.save()

                return Response(request.data, status=status.HTTP_201_CREATED)
            user.delete()
            return Response(serializer_user_profile.errors, status.HTTP_400_BAD_REQUEST)

        return Response(serializer_user.errors, status.HTTP_400_BAD_REQUEST)


class UserCompletedTopicsView(APIView):
    def get(self, request, user_id, *args, **kwargs):
        user = UserProfile.objects.get(id=user_id)
        if not user:
            return Response({"res": "User does not exist"}, status=status.HTTP_400_BAD_REQUEST)

        topics = Topic.objects.filter(completed_topics__in=user.completed_topics.all())

        serializer = TopicSmallSerializer(topics, many=True)
        print(user.completed_topics.all().values())
        print(serializer.data)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, user_id, *args, **kwargs):
        user = UserProfile.objects.get(id=user_id)
        topic = Topic.objects.get(id=request.data.get('id'))

        if not user or not topic:
            return Response({"res":"Topic or user does not exist"}, status=status.HTTP_400_BAD_REQUEST)

        completed_topic = CompletedTopic.objects.create()
        completed_topic.user = user
        completed_topic.topic = topic
        completed_topic.save()

        user.completed_topics.add(completed_topic)
        user.save()

        return Response(status=status.HTTP_200_OK)

    def delete(self, request, user_id, topic_id, *args, **kwargs):
        user = UserProfile.objects.get(id=user_id)
        topic = Topic.objects.get(id=topic_id)

        if not user or not topic:
            return Response({"res":"Topic or user does not exist"}, status=status.HTTP_400_BAD_REQUEST)

        completedTopic = CompletedTopic.objects.get(user=user, topic=topic)

        if not completedTopic:
            return Response({"res": "User has not complted that topic"}, status=status.HTTP_400_BAD_REQUEST)

        completedTopic.delete()

        user.save()
        topic.save()

        return Response({"res": "Uncompleted the toopic"}, status=status.HTTP_200_OK)


class UserFavouritedTopicsView(APIView):
    def get(self, request, user_id, *args, **kwargs):
        user = UserProfile.objects.get(id=user_id)
        if not user:
            return Response({"res": "User does not exist"}, status=status.HTTP_400_BAD_REQUEST)

        topics = Topic.objects.filter(favourited_topics__in=user.favourited_topics.all())

        serializer = TopicSmallSerializer(topics, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, user_id, *args, **kwargs):
        user = UserProfile.objects.get(id=user_id)
        topic = Topic.objects.get(id=request.data.get('id'))

        if not user or not topic:
            return Response({"res":"Topic or user does not exist"}, status=status.HTTP_400_BAD_REQUEST)

        favourited_topic = FavouritedTopic.objects.create()
        favourited_topic.user = user
        favourited_topic.topic = topic
        favourited_topic.save()

        user.favourited_topics.add(favourited_topic)
        user.save()

        return Response(status=status.HTTP_200_OK)

    def delete(self, request, user_id, topic_id, *args, **kwargs):
        user = UserProfile.objects.get(id=user_id)
        topic = Topic.objects.get(id=topic_id)

        if not user or not topic:
            return Response({"res":"Topic or user does not exist"}, status=status.HTTP_400_BAD_REQUEST)

        favouritedTopic = FavouritedTopic.objects.get(user=user, topic=topic)

        if not favouritedTopic:
            return Response({"res": "User has not complted that topic"}, status=status.HTTP_400_BAD_REQUEST)

        favouritedTopic.delete()

        user.save()
        topic.save()

        return Response({"res": "Un-favourited the toopic"}, status=status.HTTP_200_OK)

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




