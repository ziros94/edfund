from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import User, School, Fund, Donation, Club, Incentive, decode_id
from .forms import UserForm, ClubForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


def index(request):
    return render(request, 'app/index.html', {})


class SchoolsView(generic.ListView):
    template_name = 'app/schools/schools.html'
    model = School


class ClubsView(generic.ListView):
    template_name = 'app/schools/clubs.html'
    model = Club

    def get_queryset(self):
        if self.args:
            return Club.objects.filter(school__id=decode_id(self.args[0]))
        else:
            return Club.objects.all()


class FundsView(generic.ListView):
    template_name = 'app/schools/funds.html'
    model = Fund

    def get_queryset(self):
        if self.args:
            return Fund.objects.filter(club__id=decode_id(self.args[1]))
        else:
            return Fund.objects.all()


class FundView(generic.DetailView):
    template_name = 'app/schools/fund.html'
    model = Fund

    def get_object(self):
        return get_object_or_404(Fund, pk=decode_id(self.args[2]))


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
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            registered = True
            print "REGISTER SUCCESS"
        else:
            print user_form.errors
    else:
        user_form = UserForm()
    return render(request, 'app/registration/register.html', {'user_form': user_form, 'registered': registered})


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
            # club = club_form.save()
            school = get_object_or_404(School, pk=int(request.POST['school_select']))
            print school.school_name, request.user.id
            club = Club(club_name=club_form.cleaned_data['club_name'], description=club_form.cleaned_data['description'], school=school, leader=request.user)
            # club.school = school
            # club.leader = user
            club.save()
            return HttpResponseRedirect('/edfund/clubs/')
        else:
            print club_form.errors
    else:
        club_form = ClubForm()
        schools = School.objects.all()
        return render(request, 'app/user/addclub.html', {'club_form': club_form, 'schools': schools})