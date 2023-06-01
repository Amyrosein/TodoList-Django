from django import forms


class TodoForm(forms.Form):
	add_todo = forms.CharField(label=" ", required=False, max_length=255,widget=forms.TextInput(attrs={'placeholder': 'بنویس و اینتر بزن ...'}))


class UpdateTodoForm(forms.Form):
	description = forms.CharField(label=" ", required=False)
