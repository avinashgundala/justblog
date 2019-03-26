from django.urls import path,include,re_path
from .views import (
                     PostListAPIView,
                     PostDetailAPIView,
                     PostUpdateAPIView,
                     PostDeleteAPIView,
                     PostCreateAPIView,
                                         )

urlpatterns = [
    path('',PostListAPIView.as_view(),name='api-list'),
    path('<int:pk>/',PostDetailAPIView.as_view(),name='api-detail'),
    path('<int:pk>/update/',PostUpdateAPIView.as_view(),name='api-update'),
    path('<int:pk>/delete/',PostDeleteAPIView.as_view(),name='api-delete'),
    path('create/',PostCreateAPIView.as_view(),name='api-create'),
]
