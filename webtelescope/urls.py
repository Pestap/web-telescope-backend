"""
URL configuration for webtelescope project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from mainapp.views import *


urlpatterns = [
    path('photos/<int:photo_id>', PhotoDetailApiView.as_view()),
    path('sections', SectionView.as_view()),
    path('sections/<int:section_id>', SectionDetailView.as_view()),
    path('chapters/<int:chapter_id>', ChapterDetailView.as_view()),
    path('topics/<int:topic_id>', TopicDetailView.as_view()),
    path('paragraphs/<int:paragraph_id>', ParagraphDetailView.as_view()),
    path('tests/<int:test_id>', TestDetailView.as_view()),
    path('questions/<int:question_id>', QuestionDetailView.as_view()),
    path('answers/<int:answer_id>', AnswerDetailViewNoResult.as_view()),
    path('answers/<int:answer_id>/check', AnswerDetailViewResult.as_view()),
    path('users/<int:user_id>', UserDetailView.as_view()),
    path('users/<int:user_id>/scores', UserScoreView.as_view()),
    path('admin', admin.site.urls),
    path('admin/', admin.site.urls),
]
