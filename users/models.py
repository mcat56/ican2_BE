from django.db import models

# Create your models here.
class Users(models.Model):
    name = models.TextField()
    email = models.TextField()
    password_digest = models.TextField()
    location = models.TextField()
    meetup_radius = models.IntegerField()
    current_field_of_work = models.TextField()
    experience_level = models.TextField()
    mentee = models.BooleanField()
    mentor = models.BooleanField()
    about_me = models.TextField()
    gender = models.TextField()
    picture = models.TextField()
    work_day = models.TextField()
    enjoyment = models.TextField()
    teaching_points = models.TextField()
    advice = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
