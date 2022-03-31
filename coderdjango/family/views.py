from django.views.generic import TemplateView
from django.shortcuts import render
from .models import FamilyMember

# class FamilyView(TemplateView):
#     template_name = "family/index.html"
#This approach didn´t work for me, need more debugging time to make it work.


def family_members(request, status=None):
    context = {"family" : FamilyMember.objects.all()}
    return render(request, "family/index.html", context = context)
    