from django.db.models import Count
from django.http import HttpResponse
from django.shortcuts import render

from OtidiDo.ideas.models import Idea


# Create your views here.

def home(request):
    top_ideas = Idea.objects.annotate(num_likes=Count('likes')).order_by('-num_likes')[:3]
    return render(request, 'common/base.html', {'top_ideas': top_ideas})

