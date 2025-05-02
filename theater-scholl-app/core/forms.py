# theater-scholl-app/core/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserProfile, TheatricalPerformance, Course, Instructor, Student, Review

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['text', 'approved']

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'profile_data']

class InstructorForm(forms.ModelForm):
    class Meta:
        model = Instructor
        fields = ['name', 'specialization']

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['title', 'instructor', 'schedule']

class PerformanceForm(forms.ModelForm):
    class Meta:
        model = TheatricalPerformance
        fields = ['title', 'date', 'description']

class RegistrationForm(UserCreationForm):
    full_name = forms.CharField(max_length=255, required=True, label="ФИО")
    avatar = forms.ImageField(required=False, label="Фото профиля")
    class Meta:
        model = UserProfile
        fields = ("username", "full_name", "avatar", "password1", "password2")

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ["full_name", "avatar", "contact_info"]

class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']
