from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_blog, name='create_blog'),
    path('doctor/', views.doctor_blogs, name='doctor_blogs'),
    path('edit/<int:blog_id>/', views.edit_blog, name='edit_blog'),
    path('delete/<int:blog_id>/', views.delete_blog, name='delete_blog'),
    path('patient/', views.patient_blogs, name='patient_blogs'),
    path('detail/<int:blog_id>/', views.blog_detail, name='blog_detail'),
]
