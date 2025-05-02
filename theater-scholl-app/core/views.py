# Файл: theater-scholl-app/core/views.py
from django.core.mail import send_mail
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import RegistrationForm, ProfileForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from courses.models import Course
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect, get_object_or_404
from .models import TheatricalPerformance, Course, Instructor, Student, Review
from .forms import PerformanceForm, CourseForm, InstructorForm, StudentForm
from django.contrib import messages

from django.contrib import messages
from django.contrib.messages import get_messages

from django.contrib.messages import get_messages

from django.contrib import messages

from django.contrib.messages import get_messages

def user_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("dashboard")
        else:
            messages.error(request, "Пользователь не найден")
            storage = get_messages(request)
            for message in storage:
                print(f"DEBUG MESSAGE: {message}")  # Проверка, передаётся ли ошибка

            return redirect("login")

    return render(request, "core/login.html")






def is_admin(user):
    return user.is_superuser

def is_admin(user):
    return user.is_staff

def is_instructor(user):
    return user.role == 'instructor' or user.is_staff  # Преподаватель или админ

def is_student(user):
    return user.role == 'student' and not user.is_staff  # Только студенты

@login_required
@user_passes_test(is_admin)
def admin_dashboard(request):
    return render(request, 'core/admin_dashboard.html')

@login_required
@user_passes_test(is_instructor)
def instructor_dashboard(request):
    return render(request, 'core/instructor_dashboard.html')

@login_required
@user_passes_test(is_student)
def student_dashboard(request):
    return render(request, 'core/student_dashboard.html')

@login_required
@user_passes_test(is_admin)
def approve_review(request, id):
    review = get_object_or_404(Review, id=id)
    review.approved = True
    review.save()
    return redirect('admin_dashboard')

@login_required
@user_passes_test(is_admin)
def delete_review(request, id):
    review = get_object_or_404(Review, id=id)
    review.delete()
    return redirect('admin_dashboard')

@login_required
@user_passes_test(is_admin)
def create_student(request):
    form = StudentForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('admin_dashboard')
    return render(request, 'core/admin_form.html', {'form': form})

@login_required
@user_passes_test(is_admin)
def edit_student(request, id):
    student = get_object_or_404(Student, id=id)
    form = StudentForm(request.POST or None, instance=student)
    if form.is_valid():
        form.save()
        return redirect('admin_dashboard')
    return render(request, 'core/admin_form.html', {'form': form})

@login_required
@user_passes_test(is_admin)
def delete_student(request, id):
    student = get_object_or_404(Student, id=id)
    student.delete()
    return redirect('admin_dashboard')

@login_required
@user_passes_test(is_admin)
def create_instructor(request):
    form = InstructorForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('admin_dashboard')
    return render(request, 'core/admin_form.html', {'form': form})

@login_required
@user_passes_test(is_admin)
def edit_instructor(request, id):
    instructor = get_object_or_404(Instructor, id=id)
    form = InstructorForm(request.POST or None, instance=instructor)
    if form.is_valid():
        form.save()
        return redirect('admin_dashboard')
    return render(request, 'core/admin_form.html', {'form': form})

@login_required
@user_passes_test(is_admin)
def delete_instructor(request, id):
    instructor = get_object_or_404(Instructor, id=id)
    instructor.delete()
    return redirect('admin_dashboard')

def is_admin(user):
    return user.is_staff

@login_required
@user_passes_test(is_admin)
def create_course(request):
    form = CourseForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('admin_dashboard')
    return render(request, 'core/admin_form.html', {'form': form})

@login_required
@user_passes_test(is_admin)
def edit_course(request, id):
    course = get_object_or_404(Course, id=id)
    form = CourseForm(request.POST or None, instance=course)
    if form.is_valid():
        form.save()
        return redirect('admin_dashboard')
    return render(request, 'core/admin_form.html', {'form': form})

@login_required
@user_passes_test(is_admin)
def delete_course(request, id):
    course = get_object_or_404(Course, id=id)
    course.delete()
    return redirect('admin_dashboard')

@login_required
@user_passes_test(is_admin)
def create_performance(request):
    form = PerformanceForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('admin_dashboard')
    return render(request, 'core/admin_form.html', {'form': form})

@login_required
@user_passes_test(is_admin)
def edit_performance(request, id):
    performance = get_object_or_404(TheatricalPerformance, id=id)
    form = PerformanceForm(request.POST or None, instance=performance)
    if form.is_valid():
        form.save()
        return redirect('admin_dashboard')
    return render(request, 'core/admin_form.html', {'form': form})

@login_required
@user_passes_test(is_admin)
def delete_performance(request, id):
    performance = get_object_or_404(TheatricalPerformance, id=id)
    performance.delete()
    return redirect('admin_dashboard')

def contacts(request):
    return render(request, 'core/contacts.html')

def home(request):
    return render(request, 'core/index.html')

def courses_list(request):
    """ Представление для списка курсов. """
    courses = Course.objects.all()  # Загружаем список курсов
    return render(request, "core/courses_list.html", {"courses": courses})

def courses_schedule(request):
    """ Представление для отображения расписания курсов. """
    return render(request, "core/courses_schedule.html")

@login_required
def delete_account(request):
    """ Представление для удаления аккаунта. """
    user = request.user
    user.delete()
    return redirect('home')  # Перенаправление на главную после удаления

@login_required
def profile(request):
    user = request.user
    if request.method == "POST":
        form = ProfileForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect("profile")
    else:
        form = ProfileForm(instance=user)
    return render(request, "core/profile.html", {"form": form})

def index(request):
    return render(request, 'core/index.html')

def about(request):
    return render(request, 'core/about.html')

def courses(request):
    return render(request, "courses/courses.html")

def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")
    else:
        form = RegistrationForm()

    return render(request, "core/register.html", {"form": form})

def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        # Отправка email
        send_mail(
            subject=f"Сообщение от {name}, {email}",
            message=message,
            from_email=email,
            recipient_list=["ragel.alexandr@gmail.by"],  # Замени на нужный email
        )

        messages.success(request, "Ваше сообщение отправлено!")

    return render(request, "core/contact.html")




