from .models import SettingsConfig, SocialMediaURL, SocialMediaTypeChoice
from about_me.models import AboutMe

def website_setting(request):
    website_settings = SettingsConfig.objects.all().first()
    social_links = SocialMediaURL.objects.filter(type=SocialMediaTypeChoice.PERSON)
    about_me = AboutMe.objects.all().first()
    print(about_me)
    return {'website_settings': website_settings, 'social_links': social_links, 'about_me': about_me}

