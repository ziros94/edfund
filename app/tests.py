from django.test import TestCase
from .models import User, School, Fund, Club, Donation, Incentive
# Create your tests here.


class UserTestCase(TestCase):
    def test_create_user(self):
        alvi = User.objects.create(username="Alvi",password="1234")
        school = School.objects.create(school_name="Tandon")
        club = Club.objects.create(club_name="Robotics", leader=alvi, school=school)
        print alvi.get_username()
        self.assertEqual(school.club_set.get(pk=club.id), club)
