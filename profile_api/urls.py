from django.urls import path, include

from rest_framework.routers import DefaultRouter

from profile_api import views


router = DefaultRouter()
router.register('hello-viewset',views.HelloViewSet, basename='hello-viewset')
router.register('profile',views.UserProfileViewSet) #No need to give basename because queryset is given in the UserProfileViewSet

urlpatterns = [
    path('hello-view/',views.HelloApiView.as_view()),        #First it'll check the /api and then check /hello-view
    path('login/',views.UserLoginApiView.as_view()),
    path('',include(router.urls))

]
