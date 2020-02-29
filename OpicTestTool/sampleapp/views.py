from random import randint

from django.shortcuts import HttpResponse, render, redirect

from .models import Question
from .forms import QuestionForm, QuestionChoiceForm, NoteForm, TTSContextForm

from .core.TTS import TTS
from .core.Utils import Singleton


class _CurrentQuestion(object):
    __metaclass__ = Singleton

    def __init__(self):
        self.index = 1
        self.type = "------------------------------"


_current_question = _CurrentQuestion()


def practice_page(request):
    if request.method == "GET":
        obj = Question.objects.all().get(type=_current_question.type)

        question_type = obj.type
        question = obj.question

        note = NoteForm()
        note.fields['sample_answer'].initial = obj.sample_answer
        note.fields['description'].initial = obj.description

        choices = QuestionChoiceForm()
        choices.fields['question_types'].initial = _current_question.index

        question_adding_form = QuestionForm()

        context = {
            "question_type": question_type,
            "question": question,
            "note": note,
            "choices": choices,
            "question_adding_form": question_adding_form,
        }
        return render(request, 'practice.html', context)

    return HttpResponse("<H1>Can not Support this Request</H1>", status=404)


def exam_page(request):
    if(request.method == "GET"):
        return render(request, 'exam.html')


def util_page(request):
    if(request.method == "GET"):
        context = {
            "form": TTSContextForm()
        }
        return render(request, 'util.html', context)
    else:
        form = TTSContextForm(request.POST)
        if form.is_valid():
            context = form.cleaned_data['context']

            _tts = TTS(context)
            response = HttpResponse(
                _tts.text_to_speach(), content_type='audio/mpeg')
            response['Content-Disposition'] = "attachment; filename=TTS.mp3"
            return response

        return HttpResponse("<H1> Page Error </H1>")


def selected_question(request):
    if(request.method == "GET"):
        return HttpResponse("<H1>Can not Support this Request</H1>", status=404)
    else:
        choice = QuestionChoiceForm(request.POST)
        if choice.is_valid():
            _current_question.index = int(
                choice.cleaned_data['question_types'])
            _current_question.type = dict(choice.fields['question_types'].choices)[
                _current_question.index]
            return redirect('practice_page')
        else:
            return HttpResponse("<H1> Select Question Error </H1>")


def random_question(request):
    if(request.method == "GET"):
        return HttpResponse("<H1>Can not Support this Request</H1>", status=404)
    else:
        questions = list(Question.objects.values_list(
            'type'))
        _current_question.index = randint(2, len(questions))
        _current_question.type = questions[_current_question.index - 1][0]

        return redirect('practice_page')


def add_question(request):
    if(request.method == "GET"):
        return HttpResponse("<H1>Can not Support this Request</H1>", status=404)
    else:
        return HttpResponse("<H1>Can not Support this Request</H1>", status=404)


def delete_question(request):
    if(request.method == "GET"):
        return HttpResponse("<H1>Can not Support this Request</H1>", status=404)
    else:
        if _current_question.index != 1:
            obj = Question.objects.get(type=_current_question.type)
            obj.delete()
            _current_question.index = 1
            _current_question.type = "------------------------------"

        return redirect('practice_page')


def update_question(request):
    if(request.method == "GET"):
        return HttpResponse("<H1>Can not Support this Request</H1>", status=404)
    else:
        note = NoteForm(request.POST)
        if note.is_valid():
            _sample_answer = note.cleaned_data['sample_answer']
            _description = note.cleaned_data['description']

            obj = Question.objects.get(type=_current_question.type)
            obj.sample_answer = _sample_answer
            obj.description = _description
            obj.save()

            return redirect('practice_page')
        else:
            return HttpResponse("<H1> Select Question Error </H1>")
