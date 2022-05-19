from django.urls import path

from family_members import views

urlpatterns = [
    #path('index-1', views.index1),
    #path('get-course-1/<int:id>/', views.get_course1),
    #path('post-course-1/<str:name>/<int:code>/', views.post_course1),
    #path('all-courses-1/', views.all_courses1),

    path('index', views.index),
    path('get_member/<int:id>/', views.get_member, name='member'),
    #path('get_member/<int:id>/', views.get_member),
    #path('post-course-2/<str:name>/<int:code>/', views.post_course2),
    path('all-members/', views.all_members),
    #path('cursos', views.cursos),
]