from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver


@login_required
def home(request):
    return render(request, "goroskop/home.html")


