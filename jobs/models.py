from django.db import models

class Job(models.Model):
    title = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    description = models.TextField()
    
    def __str__(self):
        return self.title

class Application(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    resume_link = models.URLField(help_text="Google Drive Link")

    def __str__(self):
        return f"{self.name} - {self.job.title}"