from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import feedback_form, get_categories_by_building, fetch_feedback_entries

from django_otp.admin import OTPAdminSite
from django_otp.plugins.otp_totp.models import TOTPDevice
from django_otp.plugins.otp_totp.admin import TOTPDeviceAdmin
from .models import CustomUser

class OTPAdmin(OTPAdminSite):
    pass

admin_site = OTPAdmin(name='OTPAdmin')
admin_site.register(CustomUser)
admin_site.register(TOTPDevice, TOTPDeviceAdmin)


urlpatterns = [
    path('', views.Index, name='index'),
    path('about/', views.About, name='about'),
    path('feedback_form/', views.feedback_form, name='feedback_form'),
    path('dashboard/', views.mydashboard, name='dashboard'),
    path('dashboard/<int:category_id>/', views.mydashboard, name='dashboard_category'),

    path('dashboard_hinang/', views.mydashboard2, name='dashboard2'),
    path('dashboard_villares/', views.mydashboard3, name='dashboard3'),
    path('dashboard_kinaadman/', views.mydashboard4, name='dashboard4'),
    path('dashboard_nsb/', views.mydashboard5, name='dashboard5'),
    path('dashboard_iwag/', views.mydashboard6, name='dashboard6'),
    path('dashboard_masawa/', views.mydashboard7, name='dashboard7'),
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('feedback/', feedback_form, name='feedback_form'),
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('admin/', admin_site.urls),
    path('logout/', views.logout_user, name='logout'),

    path('get_categories_by_building/', get_categories_by_building, name='get_categories_by_building'),
    path('api/feedback_entries/', get_categories_by_building, name='get_category_feedback_entries'),


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