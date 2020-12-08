from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.utils import timezone
from django.forms import inlineformset_factory
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


from .models import *
from .forms import  *

# Create your views here.
class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = 'latest_question_list'
    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')
    
    # def get_context_data(self, *args, **kwargs):
    #     context = super().get_context_data(*args, **kwargs)
    #     if self.request.user.is_authenticated:  
    #         context['username'] = self.request.user.username  
    #     return context
        
class VotesView(generic.ListView):
    template_name = "polls/votes.html"
    context_object_name = "votes_list"
    def get_queryset(self):
        return Question.objects.all().order_by('-pub_date')

class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/detail.html"
    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now())

class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

class QuestionCreate(LoginRequiredMixin, generic.View):
    raise_exception = True
    def get(self, request):
        form = QuestionForm()
        return render(request, 'polls/question_create.html', {'form':form})

    def post(self, request):
        form = QuestionForm(request.POST)
        if form.is_valid():
            new_question = form.save()
            return redirect(reverse('polls:question_create_finish', kwargs={'pk': new_question.pk},))
        return render(request, 'polls/question_create.html', context={'form':form})

@login_required
def create_question_finish(request, pk):
    QuestionFinishForm = inlineformset_factory(Question, Choice, form=ChoiceForm,)
    question = Question.objects.get(pk=pk)
    # print(question)
    # print(question.id)
    if request.method == "POST":
        # print(request.POST)
        # formset = ChoiceForm(request.POST)
        formset = QuestionFinishForm(request.POST, instance=question)

        if formset.is_valid():
            # new_choice = formset.save(commit=False)
            # new_choice.question_id = pk
            # new_choice.save()
            formset.save()
            return redirect('polls:index')
    else:
        # print(request.POST)
        # formset = ChoiceForm()
        formset = QuestionFinishForm(instance=question)
    context = {'formset': formset, 'question': question}
    return render(request, 'polls/quetion_create_finish.html', context)

from django.contrib.auth.forms import AuthenticationForm  
from django.contrib import auth  
from django.urls import reverse_lazy  

def login(request):  
    if request.method == 'POST':  
        form = RFPAuthForm(request=request, data=request.POST)  
        if form.is_valid():  
            auth.login(request, form.get_user())  
            return HttpResponseRedirect(reverse_lazy('polls:index'))  
    else:  
        context = {'form': RFPAuthForm()}  
        return render(request, 'polls/login.html', context)  
  
  
def logout(request):  
    auth.logout(request)  
    return HttpResponseRedirect(reverse_lazy('polls:index'))
