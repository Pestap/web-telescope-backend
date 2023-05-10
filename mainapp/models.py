from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
# Create your models here.

class Photo(models.Model):
    # id automatyczne
    title = models.CharField(max_length=50, default="New photo")
    alt = models.CharField(max_length=50, default="Alt photo")
    url = models.FileField(upload_to="photos/")

class Section(models.Model):
    # id automatyczne
    title = models.CharField(max_length=60, default="New section")
    summary = models.TextField(default="Summary...")
    photo = models.ForeignKey(Photo, on_delete=models.SET_NULL, related_name="section_photo", blank=True, null=True)
    time_investment = models.IntegerField(default=0)

class Chapter(models.Model):
    # id automatyczne
    title = models.CharField(max_length=60, default="New chapter")
    summary = models.TextField(default="Summary...")
    time_investment = models.IntegerField(default=0)
    section = models.ForeignKey(Section, on_delete=models.CASCADE, related_name="chapters")

class Topic(models.Model):
    # id automatyczne
    title = models.CharField(max_length=60, default="New topic")
    visits = models.IntegerField(default=0)
    time_investment = models.IntegerField(default=0)
    edit_date = models.DateTimeField()
    difficulty = models.IntegerField(default=0)
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE, related_name="topics")

class Paragraph(models.Model):
    # id automatyczne
    title = models.CharField(max_length=60, default="New section")
    text = models.TextField(default="Text...")
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name="paragraphs")

class UserProfile(models.Model):
    # id automatyczne
    role = models.CharField(max_length=30, default="user")
    email = models.CharField(max_length=40, default="default@webtelescope.com")
    level = models.IntegerField(max_length=0)
    xp = models.IntegerField(max_length=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_profile")

class CompletedTopic(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name="completed_topics")
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name="completed_topics")
    class Meta:
        unique_together = ('user', 'topic')

class FavouritedTopic(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name="favourited_topics")
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name="favourited_topics")
    class Meta:
        unique_together = ('user', 'topic')

class Authorship(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name="autorship")
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name="autorship")
    class Meta:
        unique_together = ('user', 'topic')

class ChapterPhoto(models.Model):
    photo = models.ForeignKey(Photo, on_delete=models.CASCADE, related_name="chapter_photo", blank=True, null=True)
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE, related_name="chapter_photo")
    class Meta:
        unique_together = ('photo', 'chapter')

class TopicPhoto(models.Model):
    photo = models.ForeignKey(Photo, on_delete=models.CASCADE, related_name="topic_photo", blank=True, null=True)
    topic = models.ForeignKey(Chapter, on_delete=models.CASCADE, related_name="topic_photo")
    class Meta:
        unique_together = ('photo', 'topic')

class ParagraphPhoto(models.Model):
    photo = models.ForeignKey(Photo, on_delete=models.CASCADE, related_name="paragraph_photo", blank=True, null=True)
    paragraph = models.ForeignKey(Paragraph, on_delete=models.CASCADE, related_name="paragraph_photo")
    class Meta:
        unique_together = ('photo', 'paragraph')

class Test(models.Model):
    # id automatyczne
    title = models.CharField(max_length=50, default="New test")
    number_of_questions = models.IntegerField(default=0)
    chapters = models.ManyToManyField(Chapter)

class Question(models.Model):
    # id automatyczne
    text = models.TextField(default="New question")
    photo = models.ForeignKey(Photo, on_delete=models.SET_NULL, related_name="questions", blank=True, null=True)
    test = models.ForeignKey(Test, on_delete=models.CASCADE, related_name="questions")

class Answer(models.Model):
    # id automatyczne
    text = models.TextField(default="New answer")
    is_correct = models.BooleanField(default=False)
    photo = models.ForeignKey(Photo, on_delete=models.SET_NULL, related_name="answers", blank=True, null=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="answers")

class Score(models.Model):
    value = models.IntegerField(default=0)
    date = models.DateTimeField()
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name="scores")
    test = models.ForeignKey(Test, on_delete=models.CASCADE, related_name="scores")
