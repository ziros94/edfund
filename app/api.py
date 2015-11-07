from tastypie.authorization import Authorization
from tastypie.authentication import BasicAuthentication
from tastypie.resources import ModelResource
from tastypie import fields
from .models import User, School, Fund, Donation, Club, Incentive


class UserResource(ModelResource):
    class Meta:
        queryset = User.objects.all()
        authorization = Authorization()
        excludes = ['email', 'password', 'is_active', 'is_staff', 'is_superuser']
        authentication = BasicAuthentication()
        allowed_methods = ['get']


class SchoolResource(ModelResource):
    class Meta:
        queryset = School.objects.all()
        authorization = Authorization()
        authentication = BasicAuthentication()


class ClubResource(ModelResource):
    user = fields.ForeignKey(UserResource, 'leader')
    school = fields.ForeignKey(SchoolResource, 'school')

    class Meta:
        queryset = Club.objects.all()
        authorization = Authorization()
        authentication = BasicAuthentication()


class FundResource(ModelResource):
    club = fields.ForeignKey(ClubResource, 'club')

    class Meta:
        queryset = Fund.objects.all()
        authorization = Authorization()
        authentication = BasicAuthentication()


class DonationResource(ModelResource):
    fund = fields.ForeignKey(FundResource, 'fund')

    class Meta:
        queryset = Donation.objects.all()
        authorization = Authorization()
        authentication = BasicAuthentication()


class IncentiveResouce(ModelResource):
    fund = fields.ForeignKey(FundResource, 'fund')

    class Meta:
        queryset = Incentive.objects.all()
        authorization = Authorization()
        authentication = BasicAuthentication()