"""VocabularyLearning URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from vocabularyL import views
from vocabularyL import views2

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^index', views.index),
    url(r'^$', views.index),
    url(r'^yes/(\d+)/', views.yes),
    url(r'^no/(\d+)/', views.no),
    url(r'^ok/(\d+)/', views.ok),
    url(r'^goon/', views.goon),
    url(r'^essay/', views.essay),
    url(r'^wordshow/', views2.wordshow),
    url(r'^reply.*/', views2.reply),
    url(r'^shownext/', views2.shownext),
    url(r'^retry/', views2.retry),
    url(r'^done/', views2.done),
    url(r'^edit/', views2.edit),
    url(r'^search/', views2.search),
    url(r'^save/', views2.save),
    url(r'^add_word_list/', views.add_word_list),
    url(r'^test/', views.test),

]
