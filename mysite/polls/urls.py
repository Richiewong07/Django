from django.conf.urls import url
from . import views

urlpatterns = [

    # r^$ MEANS DON'T ADD ANYTHING TO OUR URL --> 127.0.0.1/polls/
    # views.index  IS WHAT YOU WANT TO DISPLAY
    url(r'^$', views.index, name="index"),
]