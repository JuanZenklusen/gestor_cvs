from django.urls import path
from .views import index, RegisterView, profile, create_academic_data, update_academic_data, delete_academic_data, add_job, update_job, delete_job , about_me, add_course, course_update, course_delete


urlpatterns = [
    path('', index, name='index'),
    path('register/', RegisterView.as_view(), name='users-register'),
    path('profile/', profile, name='profile'),
    path('profile/academic', create_academic_data, name='academic'),
    path('profile/academic-update/<int:id>/', update_academic_data, name='update_academic_data'),
    path('profile/academic-delete/<int:id>/', delete_academic_data, name='delete_academic_data'),
    path('profile/add_job', add_job, name='add_job'),
    path('profile/update_job/<int:id>/', update_job, name='update_job'),
    path('profile/delete_job/<int:id>/', delete_job, name='delete_job'),
    path('profile/about_me', about_me, name='about_me'),
    path('profile/add_course', add_course, name='add_course'),
    path('profile/course_update/<int:id>/', course_update, name='course_update'),
    path('profile/course_delete/<int:id>/', course_delete, name='course_delete'),
]