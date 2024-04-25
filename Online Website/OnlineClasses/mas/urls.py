from django.contrib import admin
from django.urls import path
from mas import views

urlpatterns = [
    path('', views.index, name= 'home'),
    path('maths', views.maths, name= 'maths'),
    path('science', views.science, name= 'science'),
    path('coding', views.coding, name= 'coding'),
    path('student-portal', views.sp, name= 'student-portal'),
    path('contact-us', views.contact, name= 'contact-us'),
    path('pricing',views.cost,name='pricing'),
    path('become-a-teacher',views.b_a_teacher,name='become-a-teacher'),

    
]
