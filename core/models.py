from django.db import models
from django.contrib.auth.models import User


class Skills(models.Model):
    STAGE =(
        ('Basic','Basic'),
        ('Medium','Medium'),
        ('Advanced','Advanced')
        )
    title = models.CharField(max_length=200)
    stage = models.CharField(choices=STAGE, max_length=10, blank=True, null=True)

    def __str__(self) -> str:
        return self.title

class Team_Member(models.Model):
    GENDER = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Others', 'Others'),
    )
    name = models.CharField(max_length=200)
    professional_title = models.CharField(max_length=255)
    phone_number = models.TextField(blank=True, null=True)
    email = models.EmailField(max_length=255, blank=True, null=True)
    image = models.ImageField(upload_to='team_member/prof/',default='default/default_team_member_image.png', blank=True, null=True)
    cover_image = models.ImageField(upload_to='team_member/cover/', default='default/default_team_member_cover_image.jpg')
    designation = models.CharField(max_length=200, blank=True, null=True)
    short_description = models.TextField(blank=True, null=True)
    gender = models.CharField(choices=GENDER, blank=True, null=True, max_length=10)
    date_of_birth = models.DateField(blank=True, null=True)
    skills = models.ManyToManyField(Skills, blank=True)
    
    def __str__(self) -> str:
        return f"{self.name} ({self.professional_title})"


class SettingsConfig(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    sub_title = models.CharField(max_length=500, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    icon = models.ImageField(upload_to='site/', blank=True, null=True, default='default/site_icon.png')
    logo = models.ImageField(upload_to='site/', blank=True, null=True, default='default/site_logo.png')

    def __str__(self):
        return f"Settings Object - {self.pk}"

class SocialMediaPlatform(models.TextChoices):
    facebook = "facebook"
    website = "website"
    instagram = "instagram"
    twitter = "twitter"
    linkedin = "linkedin"
    github = "github"
    youtube = "youtube"

class SocialMediaURL(models.Model):
    platform = models.CharField(max_length=20, choices=SocialMediaPlatform, default=SocialMediaPlatform.facebook)
    url = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.platform} ({self.url})"

