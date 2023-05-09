from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model
from .serializer import UserSerializer
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Category, Topic, Comment
from .forms import TopicForm, CommentForm

class UserViewset(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = UserSerializer
    queryset = get_user_model().objects.all()

def index(request):
    categories = Category.objects.all()
    return render(request, 'api/index.html', {'categories': categories})

def category_topics(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    topics = Topic.objects.filter(category=category)
    return render(request, 'api/category_topics.html', {'category': category, 'topics': topics})

def topic_detail(request, topic_id):
    topic = get_object_or_404(Topic, pk=topic_id)
    comments = Comment.objects.filter(topic=topic)
    return render(request, 'api/topic_detail.html', {'topic': topic, 'comments': comments})

@login_required
def create_topic(request):
    if request.method == 'POST':
        form = TopicForm(request.POST)
        if form.is_valid():
            topic = form.save(commit=False)
            topic.user = request.user
            topic.save()
            return redirect('api:topic_detail', topic_id=topic.id)
    else:
        form = TopicForm()
    return render(request, 'api/create_topic.html', {'form': form})

@login_required
def create_comment(request, topic_id):
    topic = get_object_or_404(Topic, pk=topic_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.topic = topic
            comment.save()
            return redirect('api:topic_detail', topic_id=topic.id)
    else:
        form = CommentForm()
    return render(request, 'api/create_comment.html', {'form': form, 'topic': topic})