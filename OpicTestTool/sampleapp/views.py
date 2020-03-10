import os
from random import randint

from django.shortcuts import HttpResponse, render, redirect
from django.utils import timezone

from .models import Question
from .forms import AddQuestionForm, TitleChoiceForm, NoteForm, TTSContextForm, ExamTypeChoiceForm

from .pages.practice import Practice
from .pages.exam import Exam
from .pages.tts import TTS

from .configuration.config import QUESTION_AUDIO_PATH
from .utils.singleton import Singleton

INIT_INDEX = 1
INIT_TITLE = '------------------------------------------------------------'
INIT_NUM_OF_QUESTIONS = 0


class _CurrentQuestion(object):
    __metaclass__ = Singleton

    def __init__(self):
        self.index = INIT_INDEX
        self.title = INIT_TITLE
        self.num_of_questions = 0


_current_question = _CurrentQuestion()


def practice_page(request):
    if request.method == 'GET':

        # To show question title, question on the page
        obj = Question.objects.all().get(title=_current_question.title)
        question = {'title': obj.title, 'question': obj.question}

        # To show and update sample_answer, description
        note = NoteForm()
        note.fields['sample_answer'].initial = obj.sample_answer
        note.fields['description'].initial = obj.description

        # To choose question with titles
        title_choice = TitleChoiceForm()
        title_choice.fields['titles'].initial = _current_question.index

        # To check duplicated titles when users add question
        titles = []
        for t in list(Question.objects.values_list('title')):
            titles.append(t[0])

        # To add a new qiestion
        question_adding_form = AddQuestionForm()

        data = {
            # data
            'titles': titles,
            'question': question,
            # form
            'title_choice_form': title_choice,
            'note_form': note,
            'question_adding_form': question_adding_form
        }
        return render(request, 'practice.html', data)

    return HttpResponse('<H1>Can not Support this Request</H1>', status=404)


def exam_page(request):
    if request.method == 'GET':

        types = ExamTypeChoiceForm()
        data = {
            'types': types['types']
        }
        return render(request, 'exam.html', data)


def tts_page(request):
    if request.method == 'GET':
        data = {
            'tts_form': TTSContextForm()
        }
        return render(request, 'tts.html', data)
    elif request.method == 'POST':
        form = TTSContextForm(request.POST)
        if form.is_valid():
            context = form.cleaned_data['context']
            _tts = TTS(context)

            response = HttpResponse(
                _tts.text_to_speach(context), content_type='audio/mpeg')
            response['Content-Disposition'] = 'attachment; filename=TTS.mp3'
            return response

    return HttpResponse('<H1> Page Error </H1>')


def selected_question(request):
    if request.method == 'POST':
        choice = TitleChoiceForm(request.POST)
        if choice.is_valid():
            _current_question.index = int(
                choice.cleaned_data['titles'])
            _current_question.title = dict(choice.fields['titles'].choices)[
                _current_question.index]
            return redirect('practice_page')
        else:
            return HttpResponse('<H1> Select Question Error </H1>')

    return HttpResponse('<H1> Page Error </H1>')


def random_question(request):
    if request.method == 'POST':
        questions = list(Question.objects.values_list('title'))

        if len(questions) < 2:
            return redirect('practice_page')

        _current_question.index = randint(2, len(questions))
        _current_question.title = questions[_current_question.index - 1][0]

        return redirect('practice_page')

    return HttpResponse('<H1> Page Error </H1>')


def add_question(request):
    if request.method == 'POST':
        input_question = AddQuestionForm(request.POST)
        if input_question.is_valid():
            idx = int(input_question.cleaned_data['types'])
            _type = dict(input_question.fields['types'].choices)[idx]
            _title = input_question.cleaned_data['title']
            _question = input_question.cleaned_data['question']

            Question.objects.create(
                title=_title, type=_type, question=_question, description='',
                sample_answer='', difficulty=0, frequency=0, pub_date=timezone.now())

            _tts = TTS(_question)
            if _tts.make_question_audio(_title):
                _current_question.num_of_questions += 1
                _current_question.index = _current_question.num_of_questions + 1
                _current_question.title = _title
                return redirect('practice_page')

    return HttpResponse('<H1> Page Error </H1>')


def delete_question(request):
    if request.method == 'POST':
        if _current_question.index != 1:
            obj = Question.objects.get(title=_current_question.title)
            obj.delete()

            if os.path.isfile(QUESTION_AUDIO_PATH + _current_question.title + '.mp3'):
                os.remove(QUESTION_AUDIO_PATH +
                          _current_question.title + '.mp3')

            _current_question.num_of_questions -= 1
            _current_question.index = INIT_INDEX
            _current_question.title = INIT_TITLE

            return redirect('practice_page')

    return HttpResponse('<H1> Page Error </H1>')


def update_question(request):
    if request.method == 'POST':
        note = NoteForm(request.POST)
        if note.is_valid():
            _sample_answer = note.cleaned_data['sample_answer']
            _description = note.cleaned_data['description']

            obj = Question.objects.get(title=_current_question.title)
            obj.sample_answer = _sample_answer
            obj.description = _description
            obj.save()

            return redirect('practice_page')

    return HttpResponse('<H1> Page Error </H1>')
