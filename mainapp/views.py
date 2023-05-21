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