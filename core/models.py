from django.db import models
from django.contrib.auth.models import User
from .choice_utix import SocialMediaTypeChoice, SocialMediaPlatform, SkillStage
from .utils import compress_image, previous_image_delete_os, image_delete_os

class SiteSlider(models.Model):
    index = models.PositiveIntegerField(default=1)
    text = models.CharField(max_length=255, blank=True, null=True)
    details = models.TextField(blank=True, null=True)
    url = models.URLField(max_length=255, blank=True, null=True)
    slide = models.ImageField(upload_to='slide/', blank=True, null=True)
    is_active = models.BooleanField(default=True)
    create_at = models.DateTimeField(auto_now=True)
    update_at = models.DateTimeField(auto_now_add=True)

    def get_image_optimized(self, new_image, old_image=None):
        if new_image and new_image != old_image and hasattr(new_image, "file"):
            img = compress_image(new_image)
            return img
        return None

    def image_optimization(self, instance=None):
        slide = self.get_image_optimized(self.slide, instance.slide if instance is not None else None)
        if slide:
            self.slide = slide

    def image_update(self, instance):
        previous_image_delete_os(instance.slide, self.slide)

    def delete(self, *args, **kwargs):
        image_delete_os(self.slide)
        return super().delete(*args, **kwargs)
    
    def save(self, *args, **kwargs):
        if self.pk:
            instance = SiteSlider.objects.get(pk=self.pk)
            self.image_update(instance)
            self.image_optimization(instance)
        else:
            self.image_optimization()
        return super().save(*args, **kwargs)

    def __str__(self):
        return f"Slider - {self.index} ({self.pk})"

class Skills(models.Model):
    title = models.CharField(max_length=200)
    stage = models.CharField(choices=SkillStage, max_length=10, blank=True, null=True, default=SkillStage.MEDIUM)
    is_active = models.BooleanField(default=True)
    create_at = models.DateTimeField(auto_now=True)
    update_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title

class SettingsConfig(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    sub_title = models.CharField(max_length=500, blank=True, null=True)
    call = models.CharField(max_length=14, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    icon = models.ImageField(upload_to='site/', blank=True, null=True, default='default/site_icon.png')
    logo = models.ImageField(upload_to='site/', blank=True, null=True, default='default/site_logo.png')
    create_at = models.DateTimeField(auto_now=True)
    update_at = models.DateTimeField(auto_now_add=True)

    def get_image_optimized(self, new_image, old_image=None):
        if new_image and new_image != old_image and hasattr(new_image, "file"):
            return compress_image(new_image)
        return None

    def image_optimization(self, instance=None):
        icon = self.get_image_optimized(self.icon, instance.icon if instance is not None else None)
        logo = self.get_image_optimized(self.logo, instance.logo if instance is not None else None)

        if icon:
            self.icon = icon
        if logo:
            self.logo = logo

    def image_update(self, instance):
        previous_image_delete_os(instance.icon, self.icon)
        previous_image_delete_os(instance.logo, self.logo)

    def delete(self, *args, **kwargs):
        image_delete_os(self.icon)
        image_delete_os(self.logo)
        return super().delete(*args, **kwargs)
    
    def save(self, *args, **kwargs):
        if self.pk and SettingsConfig.objects.filter(pk=self.pk).exists():
            instance = SettingsConfig.objects.get(pk=self.pk)
            self.image_update(instance)
            self.image_optimization(instance)
        else:
            self.image_optimization()
        return super().save(*args, **kwargs)

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


