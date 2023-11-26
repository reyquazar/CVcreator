from django.urls import path
from .views import ResumeCreateView, ResumeListView

urlpatterns = [
    path('', ResumeCreateView.as_view(), name='create_resume'),
    path('resumes/', ResumeListView.as_view(), name='resume_list'),
]
