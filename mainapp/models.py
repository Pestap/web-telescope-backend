from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
# Create your models here.


class Photo(models.Model):
    # id automatyczne
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=50, default="New photo")
    alt = models.CharField(max_length=50, default="Alt photo")
    url = models.CharField(max_length=512, blank=True, null=True)

    class Meta:
        db_table = 'PHOTOS'

    @property
    def api_url(self):
        return "/photos/" + str(self.id)


class Section(models.Model):
    # id automatyczne
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=60, default="New section")
    summary = models.TextField(default="Summary...")
    photo = models.ForeignKey(Photo, on_delete=models.SET_NULL, related_name="section_photo", blank=True, null=True)
    time_investment = models.IntegerField(default=0)

    class Meta:
        db_table = 'SECTIONS'

    @property
    def api_url(self):
        return "/sections/" + str(self.id)


class Chapter(models.Model):
    # id automatyczne
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=60, default="New chapter")
    summary = models.TextField(default="Summary...")
    time_investment = models.IntegerField(default=0)
    sections = models.ForeignKey(Section, on_delete=models.CASCADE, related_name="chapters")
    photos = models.ManyToManyField(Photo, related_name="chapter_photos", through='ChapterPhoto')

    class Meta:
        db_table = 'CHAPTERS'

    @property
    def api_url(self):
        return "/chapters/" + str(self.id)


class Topic(models.Model):
    # id automatyczne
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=60, default="New topic")
    visits = models.IntegerField(default=0)
    time_investment = models.IntegerField(default=0)
    edit_date = models.DateTimeField()
    difficulty = models.CharField(max_length=60, default= "Średni")
    chapters = models.ForeignKey(Chapter, on_delete=models.CASCADE, related_name="topics")
    photos = models.ManyToManyField(Photo, related_name="topic_photos", through='TopicPhoto')

    class Meta:
        db_table = 'TOPICS'

    @property
    def api_url(self):
        return "/topics/" + str(self.id)


class Paragraph(models.Model):
    # id automatyczne
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=60, default="New section")
    text = models.TextField(default="Text...")
    topics = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name="paragraphs")
    photos = models.ManyToManyField(Photo, related_name="paragraph_photos", through='ParagraphPhoto')

    class Meta:
        db_table = 'PARAGRAPHS'

    @property
    def api_url(self):
        return "/paragraphs/" + str(self.id)


class Test(models.Model):
    # id automatyczne
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=50, default="New test")
    number_of_questions = models.IntegerField(default=0)
    chapters = models.ForeignKey(Chapter, on_delete=models.CASCADE, related_name="chapter_test")

    class Meta:
        db_table = 'TESTS'

    @property
    def api_url(self):
        return "/tests/" + str(self.id)


class UserProfile(models.Model):
    # id automatyczne
    id = models.IntegerField(primary_key=True)
    role = models.CharField(max_length=30, default="user")
    email = models.CharField(max_length=40, default="default@webtelescope.com")
    level = models.IntegerField()
    xp = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_profile")
    tests = models.ManyToManyField(Test, related_name="test_scores", through='Score')

    class Meta:
        db_table = 'USERS'


class CompletedTopic(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name="completed_topics", db_column="users_id")
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name="completed_topics", db_column="topics_id")

    class Meta:
        db_table = 'COMPLETED_TOPICS'
        constraints = [
            models.UniqueConstraint(fields=['user', 'topic'], name='unique user_topic combination - completed')
        ]


class FavouritedTopic(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name="favourited_topics", db_column='users_id')
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name="favourited_topics", db_column='topics_id')

    class Meta:
        db_table = 'FAVOURITED_TOPICS'
        constraints = [
            models.UniqueConstraint(fields=['user', 'topic'], name='unique user_topic combination - favourired')
        ]


class Authorship(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name="autorship", db_column='users_id')
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name="autorship", db_column='topics_id')

    class Meta:
        db_table = 'AUTHORSHIP'
        constraints = [
            models.UniqueConstraint(fields=['user', 'topic'], name='unique user_topic combination - authorship')
        ]


class ChapterPhoto(models.Model):
    photo = models.ForeignKey(Photo, on_delete=models.CASCADE, related_name="chapter_photo", db_column='photos_id')
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE, related_name="chapter_photo", db_column='chapters_id')

    class Meta:
        db_table = 'CHAPTERS_PHOTOS'
        constraints = [
            models.UniqueConstraint(fields=['photo', 'chapter'], name='unique photo_chapter combination')
        ]


class TopicPhoto(models.Model):
    photo = models.ForeignKey(Photo, on_delete=models.CASCADE, related_name="topic_photo", db_column='photos_id', null=True, blank=True)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name="topic_photo", db_column='topics_id')

    class Meta:
        db_table = 'TOPICS_PHOTOS'
        constraints = [
            models.UniqueConstraint(fields=['photo', 'topic'], name='unique photo_topic combination')
        ]


class ParagraphPhoto(models.Model):
    photo = models.ForeignKey(Photo, on_delete=models.CASCADE, related_name="paragraph_photo", blank=True, null=True, db_column='photos_id')
    paragraph = models.ForeignKey(Paragraph, on_delete=models.CASCADE, related_name="paragraph_photo", db_column='paragraphs_id')

    class Meta:
        db_table = 'PARAGRAPHS_PHOTOS'
        constraints = [
            models.UniqueConstraint(fields=['photo', 'paragraph'], name='unique photo_paragraph combination')
        ]



class Question(models.Model):
    # id automatyczne
    id = models.IntegerField(primary_key=True)
    question = models.TextField(default="New question")
    photo = models.ForeignKey(Photo, on_delete=models.SET_NULL, related_name="questions", blank=True, null=True)
    tests = models.ForeignKey(Test, on_delete=models.CASCADE, related_name="questions")

    class Meta:
        db_table = 'QUESTIONS'

    @property
    def api_url(self):
        return "/questions/" + str(self.id)


class Answer(models.Model):
    # id automatyczne
    id = models.IntegerField(primary_key=True)
    text = models.TextField(default="New answer")
    is_correct = models.BooleanField(default=False)
    photo = models.ForeignKey(Photo, on_delete=models.SET_NULL, related_name="answers", blank=True, null=True)
    questions = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="answers")

    class Meta:
        db_table = 'ANSWERS'

    @property
    def api_url(self):
        return "/answers/" + str(self.id)

    @property
    def api_url_check(self):
        return "/answers/" + str(self.id) + "/check"


class Score(models.Model):
    score = models.IntegerField(default=0)
    date = models.DateTimeField()
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name="scores" ,db_column='users_id')
    test = models.ForeignKey(Test, on_delete=models.CASCADE, related_name="scores", db_column='tests_id')

    class Meta:
        db_table = 'SCORES'
        constraints = [
            models.UniqueConstraint(fields=['user', 'date', 'test'], name='unique combination for test result (test, user, date)')
        ]
