from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import feedback_form, get_categories_by_building

urlpatterns = [
    path('', views.Index, name='index'),
    path('about/', views.About, name='about'),
    path('feedback_form/', views.feedback_form, name='feedback_form'),
    path('dashboard/', views.mydashboard, name='dashboard'),
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('feedback/', feedback_form, name='feedback_form'),
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', views.logout_user, name='logout'),

    path('get_categories_by_building/', get_categories_by_building, name='get_categories_by_building'),
    #change password
    path('change_password/', views.CustomPasswordChangeView.as_view(), name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(), name='changepassworddone'),

    #forget password
    path('password_reset/', views.CustomPasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done', views.CustomPasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

    #add new staff
    path('add_staff/', views.add_staff, name='add_staff'),
    path('remove_staff_members/', views.remove_staff_members, name='remove_staff_members'),
    
    #create new User
    #path('signup/', views.signup, name='signup'),
]