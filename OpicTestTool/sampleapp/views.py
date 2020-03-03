import os
from random import randint

from django.shortcuts import HttpResponse, render, redirect
from django.utils import timezone

from .models import Question
from .forms import AddQuestionForm, QuestionChoiceForm, NoteForm, TTSContextForm


from .configuration.config import QUESTION_AUDIO_PATH
from .core.TTS import TTS
from .utils.singleton import Singleton


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

        question_adding_form = AddQuestionForm()
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


def tts_page(request):
    if(request.method == "GET"):
        context = {
            "form": TTSContextForm()
        }
        return render(request, 'tts.html', context)
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

        if len(questions) < 2:
            return redirect('practice_page')

        _current_question.index = randint(2, len(questions))
        _current_question.type = questions[_current_question.index - 1][0]

        return redirect('practice_page')


def add_question(request):
    if(request.method == "GET"):
        return HttpResponse("<H1>Can not Support this Request</H1>", status=404)
    else:
        question = AddQuestionForm(request.POST)
        if question.is_valid():
            idx = int(question.cleaned_data['types'])
            _type = dict(question.fields['types'].choices)[idx]
            _question = question.cleaned_data['question']

            questions = list(Question.objects.values_list('type'))
            for i in range(0, 100):
                if questions.count(tuple([_type + str(i+1)])) == 0:
                    Question.objects.create(
                        type=_type + str(i+1), question=_question, description="", sample_answer="", difficulty=0, frequency=0, pub_date=timezone.now())

                    _tts = TTS(_question)
                    if _tts.make_question_audio(_type + str(i+1)):
                        return redirect('practice_page')
                    else:
                        break

        return HttpResponse("<H1>Can Make Your Question</H1>", status=500)


def delete_question(request):
    if(request.method == "GET"):
        return HttpResponse("<H1>Can not Support this Request</H1>", status=404)
    else:
        if _current_question.index != 1:
            obj = Question.objects.get(type=_current_question.type)
            obj.delete()
            print(QUESTION_AUDIO_PATH + _current_question.type)
            if os.path.isfile(QUESTION_AUDIO_PATH + _current_question.type + ".mp3"):
                os.remove(QUESTION_AUDIO_PATH +
                          _current_question.type + ".mp3")
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
