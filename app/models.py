from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from tastypie.models import create_api_key

models.signals.post_save.connect(create_api_key, sender=User)
# Create your models here.


class School(models.Model):
    school_name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=2)
    zip = models.CharField(max_length=5)

    def __str__(self):
        return self.school_name


class Club(models.Model):
    club_name = models.CharField(max_length=200)
    leader = models.ForeignKey(User)
    school = models.ForeignKey(School)

    def __str__(self):
        return self.club_name


class Fund(models.Model):
    fund_name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    club = models.ForeignKey(Club)

    def __str__(self):
        return self.fund_name


class Donation(models.Model):
    amount = models.DecimalField(max_digits=6, decimal_places=2)
    date = models.DateField(default=timezone.now)
    fund = models.ForeignKey(Fund)

    def __str__(self):
        return "${amount}".format(amount=self.amount)


class Incentive(models.Model):
    amount = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.CharField(max_length=200)
    fund = models.ForeignKey(Fund)

    def __str__(self):
        return "${amount}".format(amount=self.amount)