from django.test import TestCase
from django.contrib.auth.models import User
from .models import Team, Activity, Leaderboard, Workout

class BasicModelTests(TestCase):
    def test_team_creation(self):
        team = Team.objects.create(name='Test Team')
        self.assertEqual(str(team), 'Test Team')

    def test_activity_creation(self):
        activity = Activity.objects.create(name='Test', user='tester', team='Test Team')
        self.assertEqual(str(activity), 'Test by tester (Test Team)')

    def test_leaderboard_creation(self):
        lb = Leaderboard.objects.create(team='Test Team', points=100)
        self.assertEqual(str(lb), 'Test Team: 100')

    def test_workout_creation(self):
        workout = Workout.objects.create(name='Test Workout', description='Desc')
        self.assertEqual(str(workout), 'Test Workout')
