from django.db import models
from django.contrib.auth.models import User
from .choice_utix import SocialMediaTypeChoice, SocialMediaPlatform


class Skills(models.Model):
    STAGE =(
        ('Basic','Basic'),
        ('Medium','Medium'),
        ('Advanced','Advanced')
        )
    title = models.CharField(max_length=200)
    stage = models.CharField(choices=STAGE, max_length=10, blank=True, null=True)
    create_at = models.DateTimeField(auto_now=True)
    update_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title

class SettingsConfig(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    sub_title = models.CharField(max_length=500, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    icon = models.ImageField(upload_to='site/', blank=True, null=True, default='default/site_icon.png')
    logo = models.ImageField(upload_to='site/', blank=True, null=True, default='default/site_logo.png')
    create_at = models.DateTimeField(auto_now=True)
    update_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Settings Object - {self.pk}"

class SocialMediaURL(models.Model):
    type = models.CharField(max_length=20, choices=SocialMediaTypeChoice, default=SocialMediaTypeChoice.PERSON)
    platform = models.CharField(max_length=20, choices=SocialMediaPlatform, default=SocialMediaPlatform.FACEBOOK)
    url = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    create_at = models.DateTimeField(auto_now=True)
    update_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.platform} ({self.url})"

class Template(models.Model):
    title = models.CharField(max_length=255)
    create_at = models.DateTimeField(auto_now=True)
    update_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class TemplateSettingsConfiguration(models.Model):
    template = models.OneToOneField(Template, on_delete=models.SET_NULL, blank=True, null=True)
    create_at = models.DateTimeField(auto_now=True)
    update_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Template Configurations - {self.template.title}"


