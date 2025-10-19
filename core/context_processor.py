from .models import SettingsConfig, SocialMediaURL, SocialMediaTypeChoice

def website_setting(request):
    website_settings = SettingsConfig.objects.all().first()
    social_links = SocialMediaURL.objects.filter(type=SocialMediaTypeChoice.PERSON)
    return {'website_settings': website_settings, 'social_links': social_links}

