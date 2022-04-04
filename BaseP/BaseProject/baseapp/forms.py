from django import forms

from django.contrib.auth.models import User
from baseapp.models import Tasks, SubTasks1, Properties, Questions

from django.contrib.auth.forms import UserCreationForm

class NewTaskForm(forms.ModelForm):
    class Meta():
        model = Tasks
        fields = ['task_name','task_priority','task_responsible']

class NewSubTask1Form(forms.ModelForm):

    class Meta():
        model = SubTasks1
        fields = ['subtask1_name','subtask1_priority','subtask1_responsible']

class New_Property_Form(forms.ModelForm):
    class Meta():
        model = Properties
        fields = ['experience','documents','property_score']

class Question_Form(forms.ModelForm):
    class Meta():
        model = Questions
        fields = ['question','correct_answer','wrong_answer1','wrong_answer2','wrong_answer3']
'''
class Property_Form(forms.ModelForm):
    class Meta():
        model = Properties
        fields = ['experience','documents']
'''
'''
class UserForm(forms.ModelForm):

    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = Users
        fields = '__all__'
'''
'''

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ("email",)
'''
'''
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'email')

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'email')
'''
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class SignUpForm(UserCreationForm):
#    username = forms.CharField(max_length=30)
#    email = forms.EmailField(max_length=200)

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', )
