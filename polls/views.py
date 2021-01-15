from django.shortcuts import render, get_object_or_404, HttpResponse, HttpResponseRedirect
from .models import Question, Choice
from django.urls import reverse
from django.views import generic, View


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latestQuestionList'

    def get_queryset(self):
        # url若指定pageSize，则输出指定pageSize个条目，否则默认5条
        pageSize = int(self.request.GET.get('pageSize', 5))

        return Question.objects.order_by('pubDate')[:pageSize]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


class TestView(generic.View):
    # 根据函数名匹配请求方式返回内容
    def get(self, request):
        return HttpResponse('GET 请求')

    def post(self, request):
        return HttpResponse('POST 请求')

    def delete(self, request):
        return HttpResponse('DELETE ')

# def index(request):
#     latestQuestionList = Question.objects.order_by('-pubDate')[:5]
#
#     return render(request, 'polls/index.html', {
#         'latestQuestionList': latestQuestionList
#     })


# def detail(request, questionId):
#     question = get_object_or_404(Question, pk=questionId)
#
#     return render(request, 'polls/detail.html', {
#         'question': question
#     })


# def results(request, questionId):
#     question = get_object_or_404(Question, pk=questionId)
#
#     return render(request, 'polls/results.html', {
#         'question': question
#     })


def vote(request, questionId):
    question = get_object_or_404(Question, pk=questionId)

    try:
        selectedChoice = question.choice_set.get(pk=request.POST.get('choice', None))

    except(KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question,
            'errorMessage': '你没有选择任何选项'
        })

    else:
        selectedChoice.votes += 1
        selectedChoice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))