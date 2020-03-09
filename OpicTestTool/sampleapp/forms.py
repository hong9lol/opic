# -*- coding:utf-8 -*-
from django import forms
from .models import Question

QUESTION_TYPES = [
    (1, 'Introduce'),
    (2, 'Home'),
    (3, 'Park'),
    (4, 'Movie'),
    (5, 'Trip'),
    (6, 'Music'),
    (7, 'Show'),
    (8, 'Transportation'),
    (9, 'Appointment'),
    (10, 'Etc'),
    (11, 'Role-Play'),
    (12, 'Unexpected')]


class TitleChoiceForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(TitleChoiceForm, self).__init__(*args, **kwargs)
        self.fields['titles'] = forms.ChoiceField(
            choices=get_title_choices(), widget=forms.Select(attrs={'onchange': 'submit();', 'class': 'show-tick form-control noBSselec', 'style': 'background-color:#fdfdfd'}))


class NoteForm(forms.ModelForm):
    class Meta:
        model = Question
        widgets = {
            'sample_answer': forms.Textarea(attrs={'class': 'opic-sample-answer', 'style': 'background-color:#fdfdfd', 'rows': '20'}),
            'description': forms.Textarea(attrs={'class': 'opic-description', 'style': 'background-color:#fdfdfd', 'rows': '20'}),
        }
        fields = ['sample_answer', 'description']


class AddQuestionForm(forms.Form):
    types = forms.ChoiceField(choices=QUESTION_TYPES, widget=forms.Select(attrs={
        'class': 'show-tick form-control noBSselec'}))
    title = forms.CharField(widget=forms.Textarea(
        attrs={'class': 'opic-add-title', 'rows': '1'}))
    question = forms.CharField(widget=forms.Textarea(
        attrs={'class': 'opic-add-question', 'rows': '5'}))


class TTSContextForm(forms.Form):
    context = forms.CharField(widget=forms.Textarea(
        attrs={'class': 'opic-tts-context', 'rows': '30'}))


def get_title_choices():
    _titles = list(Question.objects.values_list('title'))
    for i, _ in enumerate(_titles):
        _titles[i] = (i + 1,) + _titles[i]
    return _titles
