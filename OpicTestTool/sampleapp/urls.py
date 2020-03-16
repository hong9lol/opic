from django.urls import path
from .views import practice_page, exam_page, history_page, tts_page
from .views import main_page
from .views import selected_question, random_question, add_question, delete_question, update_question

urlpatterns = [
    # Pages
    path('', main_page, name='main_page'),
    path('practice/', practice_page, name='practice_page'),
    path('exam/', exam_page, name='exam_page'),
    path('history/', history_page, name='history_page'),
    path('tts/', tts_page, name='tts_page'),

    # Practice
    path('selected_question/', selected_question, name='selected_question'),
    path('random_question/', random_question, name='random_question'),
    path('add_question/', add_question, name='add_question'),
    path('delete_question/', delete_question, name='delete_question'),
    path('update_question/', update_question, name='update_question'),
]
