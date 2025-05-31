from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('about/',views.about,name="about"),
    path('contact/',views.contact_view,name='contact'),
    path('login/',views.login,name='login'),
    path('register',views.register,name='register'),
    path('feedback/',views.feedback_view,name='feedback'),
    path('show_feedback',views.show_feedback,name='show_feedback'),
    path('delete-feedback/<int:feedback_id>/',views.delete_feedback, name='delete_feedback'),
]
