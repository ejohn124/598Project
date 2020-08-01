from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.views import View
from django.shortcuts import redirect

from django.contrib.auth import authenticate, login, logout
from django.shortcuts import get_object_or_404
from django.urls import reverse
from .models import Athlete, Injury, ATC, Exercise
import datetime
from django.utils import timezone



"""
Index/Dashboard:
Handles login page as well as the dashboards for both atc and athletes
Athlete can see injuries, exercises, and information
Atc can view all athletes and filter by name
"""
class Index(View):
	def get(self, request):
		if request.user.id and request.user.is_athlete:
			user = request.user
			athlete = Athlete.objects.get(user_id=user.id)

			athleteName = f"{athlete.user.first_name} {athlete.user.last_name}"
			injuryList = athlete.injury_set.all().filter(removedOn__isnull=True)
			injuryHistory = athlete.injury_set.all()
			exerciseList = []
			recentExercise = Exercise.objects.filter(injury__athlete_id=athlete.user_id, completedOn__gt=timezone.now()-datetime.timedelta(days=1))
			for injury in injuryList:
				exerciseList.extend(injury.exercise_set.all().filter(completedOn__isnull=True))
			context = {'injuryList': injuryList, 'exerciseList': exerciseList, 'athlete': athlete, 'injuryHistory': injuryHistory, 'recentExercise': recentExercise}

			return render(request, 'injuryTrack/athleteDashboard.html', context)
		elif request.user.id and request.user.is_atc:
			search_term = ''
			user = request.user
			if 'nameFilter' in request.GET:
				search_term = request.GET['nameFilter']
				athleteList = user.atc.school.athlete_set.filter(fullname__icontains=search_term)
			else:
				athleteList = user.atc.school.athlete_set.all()
				print(athleteList)


			sportToAthletes = {}
			for athlete in athleteList:
			    if athlete.sport in sportToAthletes:
			        sportToAthletes[athlete.sport].append(athlete)
			    else:
			        sportToAthletes[athlete.sport] = [athlete]
			print(sportToAthletes)
			context = {'athleteList': athleteList, 'sportToAthletes': sportToAthletes, 'user': user, 'search_term': search_term}
			return render(request, 'injuryTrack/atcDashboard.html', context)
		else:
			return render(request, 'injuryTrack/index.html')

	def post(self, request):
		user = authenticate(request, username=request.POST["usernameInput"], password=request.POST["passwordInput"])
		if user is not None:
			login(request, user)
		return HttpResponseRedirect(reverse("index"))


"""Handles anytime a user tries to log out"""
class Logout(View):
	def post(self, request):
		logout(request)
		return HttpResponseRedirect(reverse("index"))

"""Handles when an atc checks off an exercise for an athlete

On post calls /complete/ as an action, this view handles all the code needed
to complete an exercise from the atc side
"""
class Complete(View):
	def post(self, request, athlete_id):
		selected = request.POST.getlist("exercise")
		for i in selected:

			exercise = Exercise.objects.get(id=i)
			exercise.completedOn = timezone.now()
			exercise.save()

		return HttpResponseRedirect(reverse("athletedetails", args=[athlete_id]))

"""Handles when an athlete checks off an exercise

On post calls /complete/ as an action, this view handles all the code needed
to complete an exercise from the athlete side
"""
class Complete_Athlete(View):
	def post(self, request):
		selected = request.POST.getlist("exercise")
		for i in selected:

			exercise = Exercise.objects.get(id=i)
			exercise.completedOn = timezone.now()
			exercise.save()

		return HttpResponseRedirect(reverse("index"))


"""View of athlete's info from atc view

An atc can view any athlete, this view shows all of the athletes info and allows the
atc to create exercise, create and update injuries, and view recently completed exercises and past injuries
"""
class AtcAthleteView(View):

	def get(self, request, athlete_id):
		athlete = Athlete.objects.get(user_id=athlete_id)
		user = request.user
		atc = ATC.objects.get(user_id=user.id)
		athleteName = f"{athlete.user.first_name} {athlete.user.last_name}"
		injuryList = athlete.injury_set.all().filter(removedOn__isnull=True)
		injuryHistory = athlete.injury_set.all()
		exerciseList = []
		recentExercise = Exercise.objects.filter(injury__athlete_id=athlete.user_id, completedOn__gt=timezone.now()-datetime.timedelta(days=1))
		for injury in injuryList:
			exerciseList.extend(injury.exercise_set.all().filter(completedOn__isnull=True))
		context = {'injuryList': injuryList, 'exerciseList': exerciseList, 'athlete': athlete, 'atc': atc, 'injuryHistory': injuryHistory, 'recentExercise': recentExercise}
		return render(request, 'injuryTrack/atcAthleteView.html', context)

	def post(self, request, athlete_id):
		injury = Injury.objects.get(id=request.POST["btn-resolve"])
		injury.removedOn = timezone.now()
		injury.save()
		return HttpResponseRedirect(reverse("athletedetails", args=[athlete_id]))

"""Update Injury Information

This view populates the createInjury.html with the information of a given injury,
if the injury has been updated before you can see when it was, and you can change the injury's name
and description
"""
class UpdateInjury(View):
	def get(self, request, injury_id):
		injury = Injury.objects.get(id=injury_id)
		context = {'injury': injury}
		return render(request, 'injuryTrack/createInjury.html', context)

	def post(self, request, injury_id):
		btn = request.POST["btn-post"]
		injury = Injury.objects.get(id=injury_id)
		athlete = Athlete.objects.get(user__id=injury.athlete.user_id)
		if btn == "btn-submit":
			if request.POST["injuryName"] is not "" and request.POST["injuryDescription"] is not "":

				injury.name =  request.POST["injuryName"]
				injury.description = request.POST["injuryDescription"]
				injury.updatedOn = timezone.now()
				injury.save()
				return HttpResponseRedirect(reverse("athletedetails", args=[athlete.user_id]))
			else:
				injury = Injury.objects.get(id=injury_id)
				context = {'injury': injury}
				return render(request, 'injuryTrack/createInjury.html', context)
		else:
			return HttpResponseRedirect(reverse("athletedetails", args=[athlete.user_id]))


"""Create Injury page

Create an injury for an athlete, this is a new injury. The user must specify the injury name, date, and
give a description.
"""
class CreateInjury(View):
	def get(self, request, athlete_id):
		athlete = Athlete.objects.get(user_id=athlete_id)
		return render(request, 'injuryTrack/createInjury.html')

	def post(self, request, athlete_id):
		btn = request.POST["btn-post"]
		if btn == "btn-submit":
			if request.POST["injuryName"] is not "" and request.POST["injuryDescription"] is not "" and request.POST["injuryDate"] is not "":
				athlete = Athlete.objects.get(user_id=athlete_id)
				user = request.user
				atc = ATC.objects.get(user_id=user.id)
				injury = Injury(athlete=athlete, atc=atc, name=request.POST["injuryName"], description=request.POST["injuryDescription"], addedOn=request.POST["injuryDate"])
				injury.save()
				return HttpResponseRedirect(reverse("athletedetails", args=[athlete_id]))
			else:
				return render(request, 'injuryTrack/createInjury.html')
		else:
			return HttpResponseRedirect(reverse("athletedetails", args=[athlete_id]))


"""

"""
class CreateExercise(View):
	def get(self, request, athlete_id):
		athlete = Athlete.objects.get(user_id=athlete_id)
		injuryList = athlete.injury_set.filter(removedOn__isnull=True)

		context = {'athlete': athlete, 'injuryList': injuryList}
		return render(request, 'injuryTrack/CreateExercise.html', context)

	def post(self, request, athlete_id):
		if(request.POST["btn-post"] == "btn-cancel"):
			return HttpResponseRedirect(reverse("athletedetails", args=[athlete_id]))
		athlete = Athlete.objects.get(user_id=athlete_id)
		injuryList = athlete.injury_set.all()
		context = {'athlete': athlete, 'injuryList': injuryList}
		if request.POST["exerciseName"] is not "":
			sets = request.POST["setVal"]
			reps = request.POST["repVal"]
			durMin = request.POST["durationValMinutes"]
			durSec = request.POST["durationValSeconds"]
			injuryName = request.POST["injury"]
			injury = Injury.objects.get(id=injuryName)
			exercise = Exercise(injury=injury, name=request.POST["exerciseName"], addedOn=timezone.now())

			if sets is not "":
				sets = int(sets)
				if sets > 0:
					exercise.sets = sets
			if reps is not "":
				reps = int(reps)
				if reps > 0:
					exercise.reps = reps
			if durMin is not "":
				durMin = int(durMin)
				if durMin > 0:
					exercise.durationMinutes = durMin
			if durSec is not "":
				durSec = int(durSec)
				if durSec > 0:
					exercise.durationSeconds = durSec

			exercise.save()
			return HttpResponseRedirect(reverse("athletedetails", args=[athlete_id]))
		else:
			return render(request, 'injuryTrack/createExercise.html', context)
