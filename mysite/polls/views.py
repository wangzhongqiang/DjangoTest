from django.http import Http404
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

# Create your views here.

from django.http import HttpResponse
from django.template import loader
from django.urls import reverse

from django.views import generic
from .models import Question, Choice

from django.utils import timezone


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)
    """
    一种，效果同下一个
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))
    """
    """
    一种
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    output = ', '.join([q.question_text for q in latest_question_list])
    return HttpResponse(output)
    """
    #return HttpResponse("hello world")


def detail(request, question_id):


    question = get_object_or_404(Question,pk=question_id)
    return render(request, 'polls/detail.html', {"question": question})
    """
    效果同上，但是提示不一样
    try:
        question = Question.objects.get(pk=question_id)
    except:
        raise Http404("question does not exist")
    return render(request,'polls/detail.html',{"question":question})

    """
    #return HttpResponse("detail %s"% question_id)

def results(request, question_id):
    question = get_object_or_404(Question, pk = question_id)
    return render(request,"polls/results.html",{"question":question})
    #return HttpResponse(" results%s"% question_id)

def vote(request, question_id):
    question = get_object_or_404(Question,pk = question_id)
    try:
        select_choice = question.choice_set.get(pk = request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        return render(request, "polls/detail.html",{

            'question':question,
            'error_message':"瞅啥呢，选一个呀"
        })
    else:
        select_choice.votes += 1
        select_choice.save()

        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
    #return HttpResponse("vote   %s"% question_id)

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'
    def get_queryset(self):
        #return Question.objects.order_by('-pub_date')[:5]
        return Question.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now())

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

