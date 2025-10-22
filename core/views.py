from django.shortcuts import render
from django.views import View
from .models import TemplateSettingsConfiguration
from about_me.models import *

class HomePage(View):
    def get(self, request, *args, **kwargs):
        template_name = self.get_template_title()
        
        services = OurService.objects.filter(is_active=True)
        experiences = Experience.objects.filter(is_active=True)
        educations = Education.objects.filter(is_active=True)
        context = {
            "services": services,
            "experiences": experiences,
            "educations": educations
        }
        return render(request, f"{template_name}/index.html", context)
    
    def get_template_title(self):
        tem = TemplateSettingsConfiguration.objects.all().first()
        return tem.template.title


