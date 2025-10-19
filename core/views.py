from django.shortcuts import render
from django.views import View
from .models import TemplateSettingsConfiguration

class HomePage(View):
    def get(self, request, *args, **kwargs):
        template_name = self.get_template_title()
        return render(request, f"{template_name}/index.html")
    
    def get_template_title(self):
        tem = TemplateSettingsConfiguration.objects.all().first()
        return tem.template.title


