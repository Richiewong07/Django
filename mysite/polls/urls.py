from django.conf.urls import url
from . import views

urlpatterns = [

    # r^$ MEANS DON'T ADD ANYTHING TO OUR URL
    # views.index  IS WHAT YOU WANT TO DISPLAY
    # 127.0.0.1/polls/
    url(r'^$', views.index, name="index"),

    # SET QUESTION_ID TO A NUMBER
    # 127.0.0.1/polls/1
    url(r'^(?P<question_id>[0-9]+)/$', views.detail, name="detail"),

    # 127.0.0.1/polls/1/results
    url(r'^(?P<question_id>[0-9]+)/results$', views.results, name="results"),

    # 127.0.0.1/polls/1/votes
    url(r'^(?P<question_id>[0-9]+)/vote$', views.vote, name="vote"),
]


app_name = 'polls'