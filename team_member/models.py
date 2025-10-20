from django.db import models
from core.models import Skills
from core.choice_utix import GenderChoice
from core.utils import compress_image, previous_image_delete_os, image_delete_os

class TeamSettingConfig(models.Model):
    team_title = models.CharField(max_length=500, blank=True, null=True)
    team_icon = models.ImageField(upload_to='team/settings/', blank=True, null=True)
    team_logo = models.ImageField(upload_to='team/settings/', blank=True, null=True, default='default/team-c-logo-transparent.png')
    team_email = models.EmailField(max_length=200, blank=True, null=True)
    team_phone_number = models.CharField(max_length=14, blank=True, null=True)

    def get_image_optimized(self, new_image, old_image=None):
        if new_image and new_image != old_image and hasattr(new_image, "file"):
            return compress_image(new_image)
        return None

    def image_optimization(self, instance=None):
        team_icon = self.get_image_optimized(self.team_icon, instance.team_icon if instance is not None else None)
        team_logo = self.get_image_optimized(self.team_logo, instance.team_logo if instance is not None else None)

        if team_icon:
            self.team_icon = team_icon
        if team_logo:
            self.team_logo = team_logo

    def image_update(self, instance):
        previous_image_delete_os(instance.team_icon, self.team_icon)
        previous_image_delete_os(instance.team_logo, self.team_logo)

    def delete(self, *args, **kwargs):
        image_delete_os(self.team_icon)
        image_delete_os(self.team_logo)
        return super().delete(*args, **kwargs)

    def save(self, *args, **kwargs):
        if self.pk and TeamSettingConfig.objects.filter(pk=self.pk).exists():
            instance = TeamSettingConfig.objects.get(pk=self.pk)
            self.image_update(instance)
            self.image_optimization(instance)
        else:
            self.image_optimization()
        return super().save(*args, **kwargs)

    def __str__(self):
        return f"Team Settings Config {self.pk}"

class TeamMember(models.Model):
    name = models.CharField(max_length=200)
    professional_title = models.CharField(max_length=255)
    phone_number = models.CharField(blank=True, null=True)
    email = models.EmailField(max_length=255, blank=True, null=True)
    image = models.ImageField(upload_to='team/profile_picture/',default='default/default_team_member_image.png', blank=True, null=True)
    cover_image = models.ImageField(upload_to='team/cover/', default='default/default_team_member_cover_image.jpg')
    cv = models.FileField(upload_to='team/cv', blank=True, null=True)
    designation = models.CharField(max_length=200, blank=True, null=True)
    short_description = models.TextField(blank=True, null=True)
    gender = models.CharField(choices=GenderChoice, default=GenderChoice.MALE, max_length=10)
    date_of_birth = models.DateField(blank=True, null=True)
    skills = models.ManyToManyField(Skills)
    is_active = models.BooleanField(default=True, blank=True, null=True)
    create_at = models.DateTimeField(auto_now=True)
    update_at = models.DateTimeField(auto_now_add=True)
    
    def get_image_optimized(self, new_image, old_image=None):
        if new_image and new_image != old_image and hasattr(new_image, "file"):
            return compress_image(new_image)
        return None

    def image_optimization(self, instance=None):
        image = self.get_image_optimized(self.image, instance.image if instance is not None else None)
        cover_image = self.get_image_optimized(self.cover_image, instance.cover_image if instance is not None else None)

        if image:
            self.image = image
        if cover_image:
            self.cover_image = cover_image

    def image_update(self, instance):
        previous_image_delete_os(instance.image, self.image)
        previous_image_delete_os(instance.cover_image, self.cover_image)
        previous_image_delete_os(instance.cv, self.cv)

    def delete(self, *args, **kwargs):
        image_delete_os(self.image)
        image_delete_os(self.cover_image)
        image_delete_os(self.cv)
        return super().delete(*args, **kwargs)

    def save(self, *args, **kwargs):
        if self.pk and TeamMember.objects.filter(pk=self.pk).exists():
            instance = TeamMember.objects.get(pk=self.pk)
            self.image_update(instance)
            self.image_optimization(instance)
        else:
            self.image_optimization()
        return super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name} ({self.professional_title})"

class TeamWork(models.Model):
    member = models.ManyToManyField(TeamMember)
    title = models.CharField(max_length=255)
    short_description = models.TextField()
    industry = models.CharField(max_length=255, blank=True, null=True)
    details = models.TextField(blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    project_value = models.DecimalField(max_digits=9, decimal_places=2, blank=True, null=True)
    link =  models.URLField(blank=True, null=True)
    skills = models.ManyToManyField(Skills)
    is_active = models.BooleanField(blank=True, null=True, default=True)
    create_at = models.DateTimeField(auto_now=True)
    update_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class TeamWorkPicture(models.Model):
    work = models.ForeignKey(TeamWork, on_delete=models.CASCADE, related_name='teamworkpicture')
    image = models.ImageField(upload_to='work/team/', blank=True, null=True)
    is_active = models.BooleanField(default=True)
    create_at = models.DateTimeField(auto_now=True)
    update_at = models.DateTimeField(auto_now_add=True)

    def get_image_optimized(self, new_image, old_image=None):
        if new_image and new_image != old_image and hasattr(new_image, "file"):
            return compress_image(new_image)
        return None

    def image_optimization(self, instance=None):
        image = self.get_image_optimized(self.image, instance.image if instance is not None else None)
        if image:
            self.image = image

    def image_update(self, instance):
        previous_image_delete_os(instance.image, self.image)

    def delete(self, *args, **kwargs):
        image_delete_os(self.image)
        return super().delete(*args, **kwargs)
    
    def save(self, *args, **kwargs):
        if self.pk:
            instance = TeamWorkPicture.objects.get(pk=self.pk)
            self.image_update(instance)
            self.image_optimization(instance)
        else:
            self.image_optimization()

    def __str__(self):
        return f"Team Work Picture for {self.work.title}"

