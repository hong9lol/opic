from django.urls import path
from .views import practice_page, util_page, exam_page
from .views import selected_question, random_question, add_question, delete_question, update_question

urlpatterns = [
    path('', practice_page, name='practice_page'),
    path('exam/', exam_page, name='exam_page'),
    path('util/', util_page, name='util_page'),

    path('selected_question/', selected_question, name='selected_question'),
    path('random_question/', random_question, name='random_question'),
    path('add_question/', add_question, name='add_question'),
    path('delete_question/', delete_question, name='delete_question'),
    path('update_question/', update_question, name='update_question'),
]
