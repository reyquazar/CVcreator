from django.views.generic.edit import CreateView
from django.views.generic import ListView
from .models import Resume
from .forms import ResumeForm
from django.urls import reverse_lazy


class ResumeCreateView(CreateView):
    model = Resume
    form_class = ResumeForm
    template_name = 'resume_app/create_resume.html'
    success_url = reverse_lazy('create_resume')


class ResumeListView(ListView):
    model = Resume
    template_name = 'resume_app/resume_list.html'
    context_object_name = 'resumes'
