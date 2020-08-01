from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
from datetime import datetime
from django.utils import timezone


"""User class that extends abstract user, both ATC and athlete require a user

Using django's implemented user model, properties were added so that both atc
and athletes can have a username and password that works with django's authentication

"""
class User(AbstractUser):
	@property
	def is_atc(self):
		return hasattr(self, "atc")

	@property
	def is_athlete(self):
		return hasattr(self, "athlete")


"""Table representing schools

School table contains school id and name
"""
class School(models.Model):
	school_name = models.CharField(max_length=100)

	def __str__(self):
		return f"{self.school_name} ({self.id})"

"""Atc model

Model containing information for atcs, all atcs require to have a user and have a school associated
with them. Represents an athletic trainer
"""
class ATC(models.Model):
	school = models.ForeignKey(School, on_delete=models.CASCADE)
	user = models.OneToOneField(User, primary_key=True, on_delete=models.CASCADE)
	fullname = models.CharField(max_length=100)

	def __str__(self):
		return str(self.user)

	@property
	def link(self):
		return reverse('index')

"""Atc model

Model containing information for athletes, all athletes require to have a user and have a school associated
with them. Represents an athlete. An athlete can have varying injuries assigned and has multiple fields representing
personal information
"""
class Athlete(models.Model):
	school = models.ForeignKey(School, on_delete=models.CASCADE)
	user = models.OneToOneField(User, primary_key=True, on_delete=models.CASCADE)
	fullname = models.CharField(max_length=100)
	addedOn = models.DateTimeField(default=timezone.now(), null=True, blank=True)
	sport = models.CharField(max_length=100)
	phone = models.CharField(max_length=100, null=True, blank=True)
	emergency_contact = models.CharField(max_length=100, null=True, blank=True)

	@property
	def link(self):
		return reverse('athletedetails', args=[self.user_id])

	@property
	def newExerciseLink(self):
		return reverse('newexercise', args=[self.user_id])

	@property
	def newInjuryLink(self):
		return reverse('newinjury', args=[self.user_id])

	def __str__(self):
		return str(self.user)

"""Table for injuries

An injury can be assigned to an athlete from an atc. Injuries have an injury date, name, and description.
Injuries can be updated and resolved.
"""
class Injury(models.Model):
	athlete = models.ForeignKey(Athlete, on_delete=models.CASCADE)
	atc = models.ForeignKey(ATC, on_delete=models.CASCADE)

	name = models.CharField(max_length=100)
	description = models.TextField()

	def __str__(self):
		return f"({self.id}) {self.name}"

	@property
	def link(self):
		return reverse('injurydetails', args=[self.id])

	addedOn = models.DateTimeField(default=timezone.now())
	removedOn = models.DateTimeField(null=True, blank=True)
	updatedOn = models.DateTimeField(null=True, blank=True)

"""Table for exercises

Each exercise must be associated with an injury for an athlete. An exercise only needs a title and has
multiple fields to describe the required time/sets
"""
class Exercise(models.Model):
	injury = models.ForeignKey(Injury, on_delete=models.CASCADE)
	name = models.CharField(max_length=200)
	sets = models.PositiveIntegerField(default=0, null=True, blank=True)
	reps = models.PositiveIntegerField(default=0, null=True, blank=True)
	durationMinutes = models.PositiveIntegerField(default=0, null=True, blank=True)
	durationSeconds = models.PositiveIntegerField(default=0, null=True, blank=True)

	def __str__(self):
		return f"({self.id}): {self.name}"


	addedOn = models.DateTimeField(default=timezone.now())
	completedOn = models.DateTimeField(null=True, blank=True)
