from django.shortcuts import render
from django.http import JsonResponse
from django.views import View

class HomePage(View):
    def get(self, request, *args, **kwargs):
        return JsonResponse({"message": "Welcome to Samim Osman's Portfolio"})


