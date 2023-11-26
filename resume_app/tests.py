from django.test import TestCase
from django.urls import reverse

class ResumeViewTest(TestCase):
    def test_resume_list_view(self):
        response = self.client.get(reverse('resume_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "All Resumes")
        self.assertTemplateUsed(response, 'resume_app/resume_list.html')
