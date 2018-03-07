from django.db import models

from django.forms import ModelForm

# Create your models here.
class User(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    fullname = models.CharField(max_length=201, default=0)
    password = models.CharField(max_length=100)
    birthday = models.DateField()
    hobbies = models.TextField()
    u_desc = models.TextField()

    def save(self, *args, **kwargs):
        self.getfullname()
        super().save(*args, **kwargs)

    def getfullname(self):
        self.fullname = self.firstname + " " + self.lastname

class Group(models.Model):
    GROUP_PERMISSION_CHOICES = (
        ('ADD', 'ADDNEW'),
        ('EDIT', 'EDIT'),
        ('DEL', 'DELETE')
    )
    g_name = models.CharField(max_length=50)
    g_permission = models.CharField(
        max_length=4,
        choices=GROUP_PERMISSION_CHOICES,
    )
    g_desc = models.TextField()
    user = models.ManyToManyField(User)

    def __str__(self):
        return self.g_name

class Role(models.Model):
    ROLE_PERMISSION_CHOICE = (
        ('ADMIN', 'ADMIN'),
        ('PUBLISHER', 'PUBLISHER'),
        ('APPROVER', 'APPROVER'),
        ('MODERATOR', 'MODERATOR'),
        ('EDITOR', 'EDITOR'),
        ('CREATOR', 'CREATOR'),
    )
    r_name = models.CharField(max_length=100)
    r_desc = models.TextField()
    user = models.ManyToManyField(User)
    def __str__(self):
        return self.r_name