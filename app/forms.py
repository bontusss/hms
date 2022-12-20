from django.contrib.auth.forms import UserCreationForm
from models import Student, User
from django import forms

class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
        

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'

class StudentDetailsForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = [
            'student_name',
            'father_name',
            'enrollment_no',
            'course',
            'dob',
            'gender',
            'room']


class AllocationForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['room']

class PaymentForm(forms.Form):
    choice = forms.ModelChoiceField(queryset=Student.objects.all().filter(paid=True))

class UnpaidForm(forms.Form):
    choice = forms.ModelChoiceField(queryset=Student.objects.all().filter(paid=False))
