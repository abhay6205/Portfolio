from django.db import models

# Create your models here.
from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    tech_stack = models.CharField(max_length=200)
    github_link = models.URLField(blank=True)
    live_link = models.URLField(blank=True)
    image = models.ImageField(upload_to='projects/', blank=True)

    def __str__(self):
        return self.title


class Experience(models.Model):
    organization = models.CharField(max_length=200)
    role = models.CharField(max_length=200)
    duration = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.organization


class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Blog(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
