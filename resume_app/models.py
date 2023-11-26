from django.db import models


class Resume(models.Model):
    full_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number = models.CharField(max_length=99, blank=True, null=True)
    education = models.TextField()
    experience = models.TextField()
    skills = models.TextField()
    additional_information = models.TextField()

    def __str__(self):
        return self.full_name
