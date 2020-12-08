from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import PasswordInput, TextInput
from hropros import settings 
from django.utils import timezone, dateformat

from .models import *


class QuestionForm(forms.ModelForm):
    pub_date = forms.DateField(
        input_formats=settings.DATE_INPUT_FORMATS, 
        label="Дата публикации",
        initial=dateformat.format(timezone.localdate(), 'd/m/Y'))
    question_text = forms.CharField(label="Вопрос")


    
    pub_date.widget.attrs.update({'class': 'form-control'})
    question_text.widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = Question
        fields = ["question_text", "pub_date"]
        # labels = {
        #     "question_text": "ыфаффыа",
        #     "pub_date": "ыфаффыа",
        # }

    
        # widgets = {
        #     'question_text': forms.TextInput(attrs={'class': 'form-control'}),
        #     'pub_date': forms.DateInput(attrs={'class': 'form-control'}),
        # }

class ChoiceForm(forms.ModelForm):
    class Meta:
        model = Choice
        fields = ["choice_text",]

        widgets = {
            'choice_text': forms.TextInput(attrs={'class': 'form-control'}),
        }
        
class RFPAuthForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput(attrs={'class': 'form-control'}), label="Логин")
    password = forms.CharField(widget=PasswordInput(attrs={'class': 'form-control'}), label="Пароль")