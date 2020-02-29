# -*- coding:utf-8 -*-
from django import forms
from .models import Question


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        widgets = {
            'sample_answer': forms.Textarea(attrs={'class': 'opic-sample-answer', 'rows': '25'}),
            'description': forms.Textarea(attrs={'class': 'opic-description', 'rows': '25'}),
        }
        fields = ['type', 'question', 'sample_answer', 'description']


class QuestionChoiceForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(QuestionChoiceForm, self).__init__(*args, **kwargs)
        self.fields['question_types'] = forms.ChoiceField(
            choices=get_my_choices(), widget=forms.Select(attrs={'onchange': 'submit();', 'class': 'show-tick form-control noBSselec'}))


class NoteForm(forms.ModelForm):
    class Meta:
        model = Question
        widgets = {
            'sample_answer': forms.Textarea(attrs={'class': 'opic-sample-answer', 'rows': '20'}),
            'description': forms.Textarea(attrs={'class': 'opic-description', 'rows': '20'}),
        }
        fields = ['sample_answer', 'description']


class TTSContextForm(forms.Form):
    context = forms.CharField(widget=forms.Textarea(
        attrs={'class': 'opic-tts-context', 'rows': '30'}))


def get_my_choices():
    _question_types = list(Question.objects.values_list('type'))
    for i, _ in enumerate(_question_types):
        _question_types[i] = (i + 1,) + _question_types[i]
    return _question_types
