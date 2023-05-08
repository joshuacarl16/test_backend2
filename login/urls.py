from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView, TokenRefreshView,
)
from rest_framework.routers import DefaultRouter
from api.views import UserViewset
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('', views.index, name='index'),
    path('category/<int:category_id>/', views.category_topics, name='category_topics'),
    path('topic/<int:topic_id>/', views.topic_detail, name='topic_detail'),
    path('create_topic/', views.create_topic, name='create_topic'),
    path('topic/<int:topic_id>/create_comment/', views.create_comment, name='create_comment'),
    # path('forum/', include('forum.urls')),
]

router = DefaultRouter()
router.register('user', UserViewset, basename='user')

urlpatterns += router.urls