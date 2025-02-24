from django.contrib import admin
from django.urls import path, include
from . import views
from .views import dashboard, home, custom_logout
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    
    # Notifications
    path('notification/mark-as-read/', views.mark_notification_as_read, name='mark_notification_as_read'),
    path('notification/clear-all/', views.clear_all_notification, name='clear_all_notification'),
    
    # Student Management
    path('student/', include('student.urls')),
    
    # Authentication
    path('authentication/', include('home_auth.urls')),
    path('login/', views.login_view, name='login'),  # Ensure login URL exists
    
    # Teacher Management – use only one prefix for teachers
    path('teachers/', include('teachers.urls')),
    
    # Inbox & Departments
    path('inbox/', views.inbox, name='inbox'),
    path('departments/', include('department.urls')),
    
    path('subjects/', include('subjects.urls')),
    path('sports/', include('sports.urls')),
    path('', include('accounts.urls')),
    
    path('dashboard/', dashboard, name='dashboard'),
    path('dashboard/admin/', views.department_dashboard, name='department_dashboard'),
    path('dashboard/teacher/', views.teacher_dashboard, name='teacher_dashboard'),
    path('dashboard/student/', views.student_dashboard, name='student_dashboard'),
    
    path('transport/', include('transport.urls')),
    path('logout/', custom_logout, name='logout'),
    path('auth/', include('django.contrib.auth.urls')),
    
    path('exams/', include('exam.urls')),
    path('timetable/', include('timetable.urls')),
    
    path('', views.index, name='home'),  # Welcome page

    path('fees/', include('fees.urls', namespace='fees')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
