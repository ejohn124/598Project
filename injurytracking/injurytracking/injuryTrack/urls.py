from django.urls import path

from .views import Index, CreateInjury, UpdateInjury, CreateExercise, AtcAthleteView, Logout, Complete, Complete_Athlete

urlpatterns = [
	path('', Index.as_view(), name='index'),

	path('logout/', Logout.as_view(), name='logout'),

	path('complete_athlete/', Complete_Athlete.as_view(), name='complete_athlete'),

	path('<int:athlete_id>/details/complete/', Complete.as_view(), name='complete'),

	path('<int:athlete_id>/details/', AtcAthleteView.as_view(), name='athletedetails'),

	path('<int:athlete_id>/newinjury/', CreateInjury.as_view(), name='newinjury'),

	path('<int:injury_id>/injurydetails/', UpdateInjury.as_view(), name='injurydetails'),

	path('<int:athlete_id>/newexercise/', CreateExercise.as_view(), name='newexercise'),
]
