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
    (10, 'Recycling'),
    (11, 'Role-Play'),
    (12, 'Unexpected')]


class QuestionChoiceForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(QuestionChoiceForm, self).__init__(*args, **kwargs)
        self.fields['question_types'] = forms.ChoiceField(
            choices=get_question_choices(), widget=forms.Select(attrs={'onchange': 'submit();', 'class': 'show-tick form-control noBSselec'}))


class NoteForm(forms.ModelForm):
    class Meta:
        model = Question
        widgets = {
            'sample_answer': forms.Textarea(attrs={'class': 'opic-sample-answer', 'rows': '20'}),
            'description': forms.Textarea(attrs={'class': 'opic-description', 'rows': '20'}),
        }
        fields = ['sample_answer', 'description']


class AddQuestionForm(forms.Form):
    types = forms.ChoiceField(choices=QUESTION_TYPES, widget=forms.Select(attrs={
        'class': 'show-tick form-control noBSselec'}))
    question = forms.CharField(widget=forms.Textarea(
        attrs={'class': 'opic-add-question', 'rows': '5'}))


class TTSContextForm(forms.Form):
    context = forms.CharField(widget=forms.Textarea(
        attrs={'class': 'opic-tts-context', 'rows': '30'}))


def get_question_choices():
    _question_types = list(Question.objects.values_list('type'))
    for i, _ in enumerate(_question_types):
        _question_types[i] = (i + 1,) + _question_types[i]
    return _question_types
