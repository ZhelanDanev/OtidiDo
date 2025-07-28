from django import forms

from OtidiDo.ideas.models import Idea, Comment


class IdeaForm(forms.ModelForm):
    class Meta:
        model = Idea
        fields = ['title', 'description', 'image', 'city', 'category', 'date_event']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
            'date_event': forms.DateInput(attrs={'type': 'date'}),
        }
        labels = {
            'title': 'Заглавие',
            'description': 'Описание',
            'image': 'Снимка',
            'city': 'Град',
            'category': 'Категория',
            'date_event': 'Дата на събитието',
        }
        help_texts = {
            'image': 'Качи снимка в JPG формат'
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
        widgets = {
            'text': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Напиши коментар...'}),
        }
        labels = {
            'text': '',
        }
