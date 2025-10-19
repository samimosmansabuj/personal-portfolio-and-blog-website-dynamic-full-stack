from django.db import models
from core.models import Skills
from core.choice_utix import GenderChoice

class TeamSettingConfig(models.Model):
    team_title = models.CharField(max_length=500, blank=True, null=True)
    team_icon = models.ImageField(upload_to='team/settings/', blank=True, null=True)
    team_logo = models.ImageField(upload_to='team/settings/', blank=True, null=True, default='default/team-c-logo-transparent.png')
    team_email = models.EmailField(max_length=200, blank=True, null=True)
    team_phone_number = models.CharField(max_length=14, blank=True, null=True)

class TeamMember(models.Model):
    name = models.CharField(max_length=200)
    professional_title = models.CharField(max_length=255)
    phone_number = models.TextField(blank=True, null=True)
    email = models.EmailField(max_length=255, blank=True, null=True)
    image = models.ImageField(upload_to='team/profile_picture/',default='default/default_team_member_image.png', blank=True, null=True)
    cover_image = models.ImageField(upload_to='team/cover/', default='default/default_team_member_cover_image.jpg')
    designation = models.CharField(max_length=200, blank=True, null=True)
    short_description = models.TextField(blank=True, null=True)
    gender = models.CharField(choices=GenderChoice, default=GenderChoice.MALE, max_length=10)
    date_of_birth = models.DateField(blank=True, null=True)
    skills = models.ManyToManyField(Skills)
    is_active = models.BooleanField(default=True, blank=True, null=True)
    create_at = models.DateTimeField(auto_now=True)
    update_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
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

