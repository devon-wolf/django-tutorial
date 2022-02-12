from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import get_object_or_404, render
from .models import Question, Choice

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
    question = get_question(question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        context = {
            'question': question,
            'error_message': "You didn't select a choice"
            }
        return render(request, 'polls/detail.html', context)
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

def render_question_view(request, view_path, question_id):
	question = get_question(question_id)
	context = {'question': question}
	return render(request, view_path, context)

def get_question(question_id):
    return get_object_or_404(Question, pk=question_id)