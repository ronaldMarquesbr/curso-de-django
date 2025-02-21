from django.shortcuts import render
from .models import Topic


def index(request):
    """Página principal do Learning_Log"""
    return render(request, 'learning_logs/index.html')


def topics(request):
    """Mostra todos os assuntos"""

    topics_set = Topic.objects.order_by('date_added')
    context = {'topics': topics_set}

    return render(request, 'learning_logs/topics.html', context)


def topic(request, topic_id):
    """Mostra um único assunto com todas as suas entradas"""
    topic_fetched = Topic.objects.get(id=topic_id)
    entries = topic_fetched.entry_set.order_by('-date_added')
    context = {
        'topic': topic_fetched.text,
        'entries': entries
    }

    return render(request, 'learning_logs/topic.html', context)
