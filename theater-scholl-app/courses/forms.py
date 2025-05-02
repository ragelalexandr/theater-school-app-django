# Файл: theater-scholl-app/courses/forms.py
from django import forms
from .models import Portfolio
from .models import Enrollment
from .models import Review

class PortfolioForm(forms.ModelForm):
    class Meta:
        model = Portfolio
        fields = ["title", "description", "image", "video_link"]

class EnrollmentForm(forms.ModelForm):
    class Meta:
        model = Enrollment
        # Поля student и courses будем присваивать во view, поэтому в форме они не отображаются
        fields = ['enrollment_type', 'selected_start_date', 'selected_end_date']
        widgets = {
            'selected_start_date': forms.DateInput(attrs={'type': 'date'}),
            'selected_end_date': forms.DateInput(attrs={'type': 'date'}),
        }

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['content', 'rating']

