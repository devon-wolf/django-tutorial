from django.shortcuts import get_object_or_404, render
from .models import Question

# Create your views here.
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    return render_question_view(request, 'polls/detail.html', question_id)

def results(request, question_id):
    return render_question_view(request, 'polls/results.html', question_id)

def vote(request, question_id):
    return render_question_view(request, 'polls/vote.html', question_id)

def render_question_view(request, view_path, question_id):
	question = get_object_or_404(Question, pk=question_id)
	context = {'question': question}
	return render(request, view_path, context)