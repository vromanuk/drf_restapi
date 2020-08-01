from django.urls import path, include
from rest_framework.routers import DefaultRouter

from profiles_api import views

router = DefaultRouter()
router.register('hello_viewset', views.HelloViewSet, basename='hello_viewset')

urlpatterns = [
    path('hello/', views.HelloAPI.as_view()),
    path('', include(router.urls))
]
