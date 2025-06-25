from django.contrib.auth.decorators import login_required
from django.db.models import Count
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView
from django.http import JsonResponse
import json

from OtidiDo.accounts.models import Traveler
from OtidiDo.ideas.forms import IdeaForm, CommentForm
from OtidiDo.ideas.models import Idea, Like


# Create your views here.
class IdeaDetailView(DetailView):
    model = Idea
    template_name = 'ideas/idea_detail.html'
    context_object_name = 'idea'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        idea = self.get_object()
        traveler = Traveler.objects.get(user=self.request.user)
        context['form'] = CommentForm()
        context['comments'] = idea.comments.all().order_by('-created_at')
        context['liked'] = idea.likes.filter(user=traveler).exists()
        context['like_count'] = idea.likes.count()
        return context

    def post(self, request, *args, **kwargs):
        idea = self.get_object()
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.idea = idea
            comment.user = Traveler.objects.get(user=self.request.user)
            comment.save()
        return redirect('idea_detail', pk=idea.pk)


@login_required
def like_idea(request, pk):
    idea = get_object_or_404(Idea, pk=pk)
    traveler = Traveler.objects.get(user=request.user)
    like, created = Like.objects.get_or_create(user=traveler, idea=idea)
    if not created:
        like.delete()
    return redirect('idea_detail', pk=pk)


def search_view(request):
    query = request.GET.get("q", "")
    results = Idea.objects.filter(title__icontains=query) if query else []
    return render(request, "ideas/search_results.html", {"query": query, "results": results})





@login_required
def create_idea(request):
    if request.method == "POST":
        form = IdeaForm(request.POST, request.FILES)
        if form.is_valid():
            idea = form.save(commit=False)
            idea.user = Traveler.objects.get(user=request.user)
            idea.save()
            return redirect('idea_detail', pk=idea.pk)
    else:
        form = IdeaForm()
    return render(request, 'ideas/create_idea.html', {'form': form})

@login_required
def edit_idea(request, pk):
    traveler = Traveler.objects.get(user=request.user)
    idea = get_object_or_404(Idea, pk=pk, user=traveler)
    if request.method == "POST":
        form = IdeaForm(request.POST, request.FILES, instance=idea)
        if form.is_valid():
            form.save()
            return redirect('idea_detail', pk=idea.pk)
    else:
        form = IdeaForm(instance=idea)
    return render(request, 'ideas/edit_idea.html', {'form': form, 'idea': idea})

@login_required
def delete_idea(request, pk):
    traveler = Traveler.objects.get(user=request.user)
    idea = get_object_or_404(Idea, pk=pk, user=traveler)
    if request.method == "POST":
        idea.delete()
        return redirect('home')
    return render(request, 'ideas/delete_idea_confirm.html', {'idea': idea})
