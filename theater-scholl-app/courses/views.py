# Файл: theater-scholl-app/courses/views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Course, Enrollment, Portfolio, Review
from .forms import PortfolioForm, EnrollmentForm, ReviewForm

# Функция для отображения основной страницы курсов
def courses(request):
    return render(request, 'courses/courses.html')

# Отображение расписания курсов
def courses_schedule(request):
    # Предполагаем, что в модели Course есть поле available (True/False)
    courses_list = Course.objects.filter(available=True)
    return render(request, "courses/schedule.html", {"courses_list": courses_list})

# Отображение списка курсов
def courses_list(request):
    courses_list = Course.objects.filter(available=True)
    return render(request, "courses/courses.html", {"courses_list": courses_list}) 

# Функция для записи на курс (упрощённая)
@login_required
def enroll(request, course_id):
    course_obj = Course.objects.get(id=course_id)
    # Здесь создаём новый объект Enrollment (предполагается, что обязательным полем является ForeignKey 'course')
    Enrollment.objects.create(student=request.user, course=course_obj)
    return redirect("courses_list")

# Просмотр портфолио пользователя
@login_required
def portfolio_list(request):
    portfolios = Portfolio.objects.filter(user=request.user)
    return render(request, "courses/portfolio_list.html", {"portfolios": portfolios})

# Добавление записи в портфолио
@login_required
def add_portfolio(request):
    if request.method == "POST":
        form = PortfolioForm(request.POST, request.FILES)
        if form.is_valid():
            portfolio = form.save(commit=False)
            portfolio.user = request.user
            portfolio.save()
            return redirect("portfolio_list")
    else:
        form = PortfolioForm()

    return render(request, "courses/add_portfolio.html", {"form": form})

# Функция для более детальной записи на курс с использованием формы
@login_required
def enroll_courses(request, course_id):
    course_obj = get_object_or_404(Course, id=course_id)
    if request.method == "POST":
        form = EnrollmentForm(request.POST)
        if form.is_valid():
            enrollment = form.save(commit=False)
            enrollment.student = request.user
            enrollment.course = course_obj
            enrollment.save()
            return redirect('enrollment_history')
    else:
        # Устанавливаем начальные значения: тип курса и даты берём из объекта курса
        form = EnrollmentForm(initial={
            'enrollment_type': course_obj.course_type,
            'selected_start_date': course_obj.start_date,
            'selected_end_date': course_obj.end_date,
        })
    return render(request, 'courses/enroll_courses.html', {'form': form, 'course': course_obj})

# Просмотр истории записей студента
@login_required
def enrollment_history(request):
    enrollments = Enrollment.objects.filter(student=request.user)
    return render(request, 'courses/enrollment_history.html', {'enrollments': enrollments})

# Панель управления для преподавателя
@login_required
def teacher_dashboard(request):
    # Предполагается, что в модели Course поле instructor является ForeignKey к User,
    # поэтому фильтруем курсы, где instructor равен request.user
    teacher_courses = Course.objects.filter(instructor=request.user)
    return render(request, 'courses/teacher_dashboard.html', {'courses': teacher_courses})

# Функция для обновления статуса записи студента
@login_required
def update_enrollment_status(request, enrollment_id, new_status):
    enrollment = get_object_or_404(Enrollment, id=enrollment_id)
    # Проверяем, что текущий пользователь является преподавателем (сравнивая с полем course.instructor)
    if enrollment.course.instructor != request.user:
        return redirect('teacher_dashboard')  # или можно вернуть ошибку доступа
    # Проверяем, что переданный статус допустим
    if new_status not in dict(Enrollment.STATUS_CHOICES):
        return redirect('teacher_dashboard')
    enrollment.status = new_status
    enrollment.save()
    return redirect('teacher_dashboard')

@login_required
def add_review(request, course_id):
    course_obj = get_object_or_404(Course, id=course_id)
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.student = request.user
            review.course = course_obj
            review.save()
            # Можно перенаправить на детальную страницу курса или список курсов
            return redirect('courses_list')
    else:
        form = ReviewForm()
    return render(request, 'courses/add_review.html', {'form': form, 'course': course_obj})

@login_required
def moderate_reviews(request):
    # Только для администратора (или можно проверить request.user.is_staff)
    if not request.user.is_staff:
        return redirect('home')
    reviews = Review.objects.all().order_by('-created_at')
    return render(request, 'courses/moderate_reviews.html', {'reviews': reviews})

@login_required
def update_review_status(request, review_id, new_status):
    # Только администратор может менять статус отзыва
    if not request.user.is_staff:
        return redirect('home')
    review = get_object_or_404(Review, id=review_id)
    if new_status in dict(Review.STATUS_CHOICES):
        review.status = new_status
        review.save()
    return redirect('moderate_reviews')

