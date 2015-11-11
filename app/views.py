from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import User, School, Fund, Donation, Club, Incentive, UserProfile, decode_id
from .forms import UserForm, ClubForm, FundForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.core.urlresolvers import reverse


def index(request):
    return render(request, 'app/index.html', {})


class SchoolsView(generic.ListView):
    template_name = 'app/schools/schools.html'
    model = School


class SchoolInfoView(generic.DetailView):
    template_name = 'app/schools/school.html'
    model = School

    def get_object(self, queryset=None):
        return get_object_or_404(School, pk=decode_id(self.args[0]))


class ClubsView(generic.ListView):
    template_name = 'app/schools/clubs.html'
    model = Club

    def get_queryset(self):
        if self.args:
            return Club.objects.filter(school__id=decode_id(self.args[0]))
        else:
            return Club.objects.all()


class ClubInfoView(generic.DetailView):
    template_name = 'app/schools/club.html'
    model = Club

    def get_object(self, queryset=None):
        return get_object_or_404(Club, pk=decode_id(self.args[0]))


class FundsView(generic.ListView):
    template_name = 'app/schools/funds.html'
    model = Fund


class FundView(generic.DetailView):
    template_name = 'app/schools/fund.html'
    model = Fund

    def get_object(self, queryset=None):
        return get_object_or_404(Fund, pk=decode_id(self.args[0]))


class UserInfoView(generic.DetailView):
    template_name = 'app/user/user.html'
    model = User

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(UserInfoView, self).dispatch(*args, **kwargs)


class UserClubInfoView(generic.DetailView):
    template_name = 'app/user/club.html'
    model = Club

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(UserClubInfoView, self).dispatch(*args, **kwargs)


def register(request):
    schools = School.objects.all()
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        if user_form.is_valid():
            school = get_object_or_404(School, pk=int(request.POST['school']))
            user = user_form.save()
            user.set_password(user.password)
            userprof = UserProfile(user=user, school=school)
            user.save()
            userprof.save()
            registered = True
            print "REGISTER SUCCESS"
        else:
            print user_form.errors
    else:
        user_form = UserForm()
    return render(request, 'app/registration/register.html', {'user_form': user_form, 'registered': registered, 'schools': schools})


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                print "LOGIN SUCCESS"
                return HttpResponseRedirect('/edfund/')
            else:
                return HttpResponse("Your EdFund account is disabled.")
        else:
            print "Invalid login details: {0}, {1}".format(username, password)
            return HttpResponse("Invalid login details supplied.")
    else:
        return render(request, 'app/registration/login.html')


@login_required
def user_logout(request):
    logout(request)
    print "LOGOUT SUCCESS"
    return HttpResponseRedirect('/edfund/')


@login_required
def add_club(request):
    if request.method == 'POST':
        club_form = ClubForm(request.POST)
        if club_form.is_valid():
            print request.POST.get('school_select', False)
            school = get_object_or_404(School, pk=int(request.POST.get('school_select', False)))
            if school != request.user.userprofile.school:
                return HttpResponse("Restricted Access")
            print school.school_name, request.user.id
            club = Club(club_name=club_form.cleaned_data['club_name'], description=club_form.cleaned_data['description'], school=school, leader=request.user)
            club.save()
            return HttpResponseRedirect(reverse('edfund:schoolInfo', args=[school.encoded_id()]))
        else:
            print club_form.errors
    else:
        club_form = ClubForm()
        return render(request, 'app/user/addclub.html', {'club_form': club_form})


@login_required
def add_fund(request, club_id):
    if request.method == 'POST':
        fund_form = FundForm(request.POST)
        if fund_form.is_valid():
            club = get_object_or_404(Club, pk=club_id)
            if request.user != club.leader:
                return HttpResponse("Restricted Access")
            fund = Fund(fund_name=fund_form.cleaned_data['fund_name'], description=fund_form.cleaned_data['description'], club=club)
            fund.save()
            return HttpResponseRedirect(reverse('edfund:clubInfo', args=[club.encoded_id()]))
    else:
        fund_form = FundForm()
        club = get_object_or_404(Club, pk=decode_id(club_id))
        return render(request, 'app/user/addfund.html', {'fund_form': fund_form, 'club': club})


@login_required
def delete_club(request, club_id):
    club = get_object_or_404(Club, pk=decode_id(club_id))
    if request.user != club.leader:
            return HttpResponseRedirect(reverse('edfund:schoolInfo', args=[club.school.encoded_id()]))
    if request.method == 'POST':
        club.delete()
        return HttpResponseRedirect(reverse('edfund:schoolInfo', args=[club.school.encoded_id()]))
    else:
        return render(request,'app/schools/delete_club_confirm.html', {'club': club})