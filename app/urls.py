from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^schools/$', views.SchoolsView.as_view(), name='schools'),
    url(r'^(.+)/clubs/$', views.ClubsView.as_view(), name='clubs'),
    url(r'^(.+)/(.+)/funds/$', views.FundsView.as_view(), name='funds'),
    url(r'^(.+)/(.+)/(.+)/$', views.FundView.as_view(), name='fund'),
    url(r'^user/(?P<pk>[0-9]+)/$', views.UserInfoView.as_view(), name='userInfo'),
    url(r'^user/([0-9]+)/club/(?P<pk>[0-9]+)/$', views.UserClubInfoView.as_view(), name='userClubInfo'),
]