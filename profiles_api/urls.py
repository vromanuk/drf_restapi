from django.urls import path, include
from rest_framework.routers import DefaultRouter

from profiles_api import views

router = DefaultRouter()
router.register('hello_viewset', views.HelloViewSet, basename='hello_viewset')
router.register('profiles', views.UserProfileViewSet)
router.register('feed', views.UserProfileFeedViewSet)

urlpatterns = [
    path('hello/', views.HelloAPI.as_view()),
    path('login/', views.UserLoginAPIView.as_view()),
    path('', include(router.urls))
]
