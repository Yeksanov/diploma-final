from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from user import views as u
from expense import views as e
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),

    # Основные маршруты
    path('', include('main.urls')),

    # Пользовательские маршруты
    path('login/', u.LoginUser.as_view(), name='login'),
    path('register/', u.RegisterUser.as_view(), name='register'),
    path('logout/', u.custom_logout, name='logout'),
    path('profile/', u.profile, name='profile'),

    # Сброс пароля
    path('password-reset/', u.CustomPasswordResetView.as_view(), name='password_reset'),
    path('password-reset/done/', u.CustomPasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', u.CustomPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', u.CustomPasswordResetCompleteView.as_view(), name='password_reset_complete'),

    # Расходы и цели
    path('expenses/', e.expenses, name='expenses'),
    path('update_expense/<int:id>/', e.update_expense, name='update_expense'),
    path('delete_expense/<int:id>/', e.delete_expense, name='delete_expense'),
    path('pdf/', e.pdf, name='pdf'),
    path('financial_statistics/', e.financial_statistics, name='financial_statistics'),
    path('diagrams/', e.diagrams, name='diagrams'),
    path('goals/', e.goals, name='goals'),
    path('delete_goal/<int:goal_id>/', e.delete_goal, name='delete_goal'),
    path('home/', e.home, name='home'),



] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
