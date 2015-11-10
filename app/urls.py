from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^schools/$', views.SchoolsView.as_view(), name='schools'),
    url(r'^clubs/$', views.ClubsView.as_view(), name='clubs'),
    url(r'^school/(.+)/$', views.SchoolInfoView.as_view(), name='schoolInfo'),
    url(r'^funds/$', views.FundsView.as_view(), name='funds'),
    url(r'^club/(.+)/$', views.ClubInfoView.as_view(), name='clubInfo'),
    url(r'^fund/(.+)/$', views.FundView.as_view(), name='fundInfo'),
    url(r'^user/(?P<pk>[0-9]+)/$', views.UserInfoView.as_view(), name='userInfo'),
    url(r'^user/([0-9]+)/club/(?P<pk>[0-9]+)/$', views.UserClubInfoView.as_view(), name='userClubInfo'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^addclub/$', views.add_club, name='addClub'),
    url(r'^deleteclub/(?P<club_id>.+)/$', views.delete_club, name='deleteClub'),
    url(r'^addfund/(?P<club_id>.+)/$', views.add_fund, name='addFund'),
]