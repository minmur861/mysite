from django.shortcuts import render, redirect
from goroskop.models import Country, Sex, Age, Compatibility
from goroskop.models import UserProfile
from django.http import HttpResponse
from django.views.generic import DetailView

from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout
)
from goroskop.forms import UserLoginForm, UserRegisterForm, UserSex, UserCountry
from goroskop.forms import UserProfileRegisterForm


def login_view(request):
    next = request.GET.get('next')
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        login(request, user)
        if next:
            return redirect(next)
        return redirect('/')

    context = {
        'form': form,
    }
    return render(request, "goroskop/login.html", context)


def register_view(request):
    next = request.GET.get('next')
    user_form = UserRegisterForm(request.POST or None, request.FILES or None)
    profile_form = UserProfileRegisterForm(request.POST or None, request.FILES or None)
    sex_form = UserSex(request.POST or None)
    country_form = UserCountry(request.POST or None)

    if user_form.is_valid() and profile_form.is_valid() and sex_form.is_valid() and country_form.is_valid():
        user = user_form.save(commit=False)
        password = user_form.cleaned_data.get('password')
        user.set_password(password)
        user.save()
        sex = sex_form.save(commit=False)
        country = country_form.save(commit=False)
        profile = profile_form.save(commit=False)

        try:
            country = Country.objects.filter(country=country.country)[0]
        except:
            country.save()

        try:
            sex = Sex.objects.filter(sex=sex.sex)[0]
        except:
            sex.save()

        profile.get_zodiac()
        profile.get_age()
        profile.user = user
        profile.sex = sex
        profile.country = country
        profile.slug = user
        profile.save()
        new_user = authenticate(username=user.username, password=password)
        login(request, new_user)
        if next:
            return redirect(next)
        return redirect('/')

    context = {
        'user_form': user_form,
        'sex_form': sex_form,
        'country_form': country_form,
        'profile_form': profile_form

    }
    return render(request, "goroskop/register.html", context)


def logout_view(request):
    logout(request)
    return redirect('/')


def post_detail(request, slug):
    posts = UserProfile.objects.get(slug__iexact=slug)
    zodiac = posts.zodiac

    male_compatibility_dict = {
        'Aries': ('Scorpio'),
        'Taurus': ('Taurus', 'Leo', 'Scorpio', 'Capricorn'),
        'Gemini': ('Sagittarius'),
        'Cancer': ('Pisces'),
        'Scorpio': ('Libra'),
        'Sagittarius': ('Gemini', 'Leo', 'Scorpio', 'Sagittarius', 'Aquarius'),
        'Capricorn': ('Scorpio'),
        'Libra': ('Aries', 'Taurus', 'Gemini', 'Leo', 'Scorpio', 'Sagittarius', 'Aquarius'),
        'Virgo': ('Scorpio'),
        'Aquarius': ('Aries', 'Libra', 'Sagittarius', 'Pisces'),
        'Pisces': ('Virgo', 'Libra', 'Scorpio', 'Pisces'),
        'Leo': ('Aries', 'Leo', 'Scorpio', 'Sagittarius')
    }

    female_compatibility_dict = {
        'Aries': ('Leo', 'Libra', 'Scorpio', 'Aquarius'),
        'Taurus': ('Taurus', 'Libra', 'Scorpio'),
        'Gemini': ('Libra', 'Sagittarius'),
        'Cancer': ('Scorpio'),
        'Scorpio': ('Aries', 'Taurus', 'Leo', 'Libra', 'Scorpio', 'Sagittarius', 'Capricorn', 'Pisces'),
        'Sagittarius': ('Gemini', 'Leo', 'Libra', 'Sagittarius', 'Aquarius'),
        'Capricorn': ('Taurus', 'Scorpio'),
        'Libra': ('Scorpio', 'Aquarius', 'Pisces'),
        'Virgo': ('Pisces'),
        'Aquarius': ('Libra', 'Sagittarius'),
        'Pisces': ('Cancer', 'Aquarius', 'Pisces'),
        'Leo': ('Aries', 'Taurus', 'Leo', 'Libra', 'Sagittarius')
    }
    guys = ()
    if posts.sex == 'male':
        guys = male_compatibility_dict[str(zodiac)]
    else:
        guys = female_compatibility_dict[str(zodiac)]

    girls_and_boys = []

    for guy in guys:
        query_result = list(UserProfile.objects.filter(zodiac__zodiac=guy))
        if len(query_result):
             girls_and_boys.append(query_result)

    print(girls_and_boys)

    matching = []

    for profiles in girls_and_boys:
        for profile in profiles:
            if profile.user != posts.user and posts.sex != profile.sex:
                matching.append(profile)

    matching.sort(reverse=True)

    for profile in matching:
        print(profile.user)
        print(profile.age)
        print('----------')

    return render(request, 'goroskop/userprof.html', context={'posts': posts,'grls': matching})


def compatibility_view(request):
    posts = UserProfile.objects.all()
    return render(request, 'goroskop/home.html', context={'post': posts})