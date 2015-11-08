from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import User, School, Fund, Donation, Club, Incentive, decode_id
# Create your views here.


def index(request):
    return render(request, 'app/index.html', {})


class SchoolsView(generic.ListView):
    template_name = 'app/schools/schools.html'
    model = School


class ClubsView(generic.ListView):
    template_name = 'app/schools/clubs.html'
    model = Club

    def get_queryset(self):
        return Club.objects.filter(school__id=decode_id(self.args[0]))


class FundsView(generic.ListView):
    template_name = 'app/schools/funds.html'
    model = Fund

    def get_queryset(self):
        return Fund.objects.filter(club__id=decode_id(self.args[1]))


class FundView(generic.DetailView):
    template_name = 'app/schools/fund.html'
    model = Fund

    def get_object(self):
        return get_object_or_404(Fund, pk=decode_id(self.args[2]))


class UserInfoView(generic.DetailView):
    template_name = 'app/user/user.html'
    model = User


class UserClubInfoView(generic.DetailView):
    template_name = 'app/user/club.html'
    model = Club

