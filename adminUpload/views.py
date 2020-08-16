from django.shortcuts import render
from .models import Question, Choice
from django.shortcuts import HttpResponse
import django

# Create your views here.


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = django.template.loader.get_template('adminUpload/contents.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))
