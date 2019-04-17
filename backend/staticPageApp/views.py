from django.shortcuts import render
from django.views.generic import View

from staticPageApp.models import Page


class StaticPage(View):
    pass


class MainPage(View):
    def get(self, *args, **kwargs):
        return render(self.request, 'staticPageApp/index.html')