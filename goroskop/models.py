from django.db import models
from django.contrib.auth.models import User
import datetime
from django import forms
from django.conf import settings
from django.utils import timezone
from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
from django.urls import reverse


class Country(models.Model):
    country = models.CharField(max_length=30)

    def __str__(self):
        return self.country


class Sex(models.Model):
     sex = models.CharField(max_length=10, default="male")

     def __str__(self):
         return self.sex


class Zodiac(models.Model):
    zodiac = models.CharField(max_length=11)


    def __str__(self):
        return self.zodiac


class Age(models.Model):
    age = models.CharField(max_length=11)

    def __lt__(self, other):
        if self.age < other.age:
            return True
        else:
            return False

    def __str__(self):
        return self.age


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True,)
    name = models.CharField(max_length=20)
    birthdate = models.CharField(max_length=10)
    hobby = models.CharField(max_length=200, default=" ", blank=True, null=True,)
    country = models.ForeignKey(Country, on_delete=models.DO_NOTHING, null=True)
    sex = models.ForeignKey(Sex, on_delete=models.DO_NOTHING, blank=True, null=True)
    zodiac = models.ForeignKey(Zodiac, on_delete=models.DO_NOTHING, null=True)
    age = models.ForeignKey(Age,  on_delete=models.DO_NOTHING, null=True, blank=True)
    avatar = models.ImageField(upload_to="profiles/", blank=True,  null=True)
    slug = models.SlugField(default="url", max_length=50)

    def __str__(self):
        return self.name

    def __lt__(self, other):
        if self.age < other.age:
            return True
        else:
            return False

    def bit(self):
        if self.avatar:
            return u'<img src="%s" width="20"/>' % self.avatar
        else:
            return u'(none)'

    def get_age(self):
        current = self.birthdate.split(".")
        date = datetime.datetime.now()
        day = int(current[0])
        month = int(current[1])
        year = int(current[2])

        def gafdb(age):
            return Age.objects.filter(age=age)[0]

        if month < date.month:
            self.age = gafdb(date.year - year)
        elif month > date.month:
            self.age = gafdb(date.year - year - 1)
        elif month == date.month:
            self.age = gafdb(date.year - year) if(day <= date.day) else gafdb(date.year - year - 1)

    def get_absolute_url(self):
        return reverse('post_detail_url', kwargs={'slug': self.slug})

    def get_zodiac(self):
        current = self.birthdate.split(".")
        day = int(current[0])
        month = current[1]

        def gzfdb(zodiac):
            return Zodiac.objects.filter(zodiac=zodiac)[0]
        if month == '12':
            self.zodiac = gzfdb('Sagittarius') if (day < 22) else gzfdb('Capricorn')
        elif month == '01':
            self.zodiac = gzfdb('Capricorn') if (day < 20) else gzfdb('Aquarius')
        elif month == '02':
            self.zodiac = gzfdb('Aquarius') if (day < 19) else gzfdb('Pisces')
        elif month == '03':
            self.zodiac = gzfdb('Pisces') if (day < 21) else gzfdb('Aries')
        elif month == '04':
            self.zodiac = gzfdb('Aries') if (day < 20) else gzfdb('Taurus')
        elif month == '05':
            self.zodiac = gzfdb('Taurus') if (day < 21) else gzfdb('Gemini')
        elif month == '06':
            self.zodiac = gzfdb('Gemini') if (day < 21) else gzfdb('Cancer')
        elif month == '07':
            self.zodiac = gzfdb('Cancer') if (day < 23) else gzfdb('Leo')
        elif month == '08':
            self.zodiac = gzfdb('Leo') if (day < 23) else gzfdb('Virgo')
        elif month == '09':
            self.zodiac = gzfdb('Virgo') if (day < 23) else gzfdb('Libra')
        elif month == '10':
            self.zodiac = gzfdb('Libra') if (day < 23) else gzfdb('Scorpio')
        elif month == '11':
            self.zodiac = gzfdb('Scorpio') if (day < 22) else gzfdb('Sagittarius')


class Compatibility(models.Model):
    zodiac = models.ForeignKey(Zodiac, on_delete=models.DO_NOTHING)
    partnersex = models.CharField(Sex, max_length=7, default="male")
    pzodiac = models.CharField(max_length=40, default="Gemini")
