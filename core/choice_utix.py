from django.db import models

class GenderChoice(models.TextChoices):
    MALE = "male"
    FEMALE = "female"
    OTHERS = "others"

class SocialMediaTypeChoice(models.TextChoices):
    PERSON = "personal"
    TEAM = "team"

class SocialMediaPlatform(models.TextChoices):
    FACEBOOK = "facebook"
    WEBSITE = "website"
    INSTAGRAM = "instagram"
    TWITTER = "twitter"
    LINKEDIN = "linkedin"
    GITHUB = "github"
    YOUTUBE = "youtube"

class SkillStage(models.TextChoices):
    BASIC = "Basic"
    MEDIUM = "Medium"
    ADVANCED = "Advanced"

class CompanyLevel(models.TextChoices):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"

