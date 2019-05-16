from datetime import date
from django import forms

from .models import TodoList
from helpers.helper import get_ndays_later


class TodoListForm(forms.ModelForm):
    title = forms.CharField(label="할 일 이름", widget=forms.TextInput(attrs={'placeholder': '할 일의 이름'}))
    content = forms.CharField(label="내용", widget=forms.Textarea(attrs={'placeholder': '구체적인 내용'}))
    expired_date = forms.DateField(label="마감 기한",
                                   widget=forms.DateInput(attrs={'placeholder': 'YYYY-MM-DD'}),
                                   initial=get_ndays_later)

    def clean_expired_date(self):
        data = self.cleaned_data['expired_date']
        if data < date.today():
            raise forms.ValidationError("마감 기한은 오늘의 날짜보다 작을 수 없습니다")
        return data

    class Meta:
        model = TodoList
        fields = ['title', 'content', 'importance', 'expired_date',]
