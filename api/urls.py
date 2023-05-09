from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewset, index, category_topics, topic_detail, create_topic, create_comment

router = DefaultRouter()
router.register('user', UserViewset, basename='user')

urlpatterns = [
    path('', index, name='index'),
    path('category/<int:category_id>/', category_topics, name='category_topics'),
    path('topic/<int:topic_id>/', topic_detail, name='topic_detail'),
    path('topic/create/', create_topic, name='create_topic'),
    path('topic/<int:topic_id>/comment/', create_comment, name='create_comment'),
]

urlpatterns += router.urls
