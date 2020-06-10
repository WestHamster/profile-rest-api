from django.urls import path

from profile_api import views


urlpatterns = [
    path('hello-view/',views.HelloApiView.as_view()),        #First it'll check the /api and then check /hello-view

]
