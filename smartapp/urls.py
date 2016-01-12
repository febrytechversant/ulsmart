from django.conf.urls import url
from smartapp import views

urlpatterns = [
    url(r'^', views.SitesList.as_view()),
]