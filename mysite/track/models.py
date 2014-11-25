from django.db import models
import PIL

class Event(models.Model):
	def __str__(self):
		return (self.gender + ' ' + self.event_name)
	
	BOYS = 'B'
	GIRLS = 'G'
	CHOICES = (
		(BOYS, 'Boys'),
		(GIRLS, 'Girls'),
	)
	
	gender = models.CharField(max_length=1, choices=CHOICES, null=False)
	event_name = models.CharField(max_length=20, null=False)
	
	class Meta:
		unique_together = ('event_name', 'gender')
	
class Athlete(models.Model):
	def __str__(self):
		return (self.first_name + ' ' + self.last_name)

	FRESHMAN = 'FR'
	SOPHOMORE = 'SO'
	JUNIOR = 'JR'
	SENIOR = 'SR'
	CHOICES = (
		(FRESHMAN, 'Freshman'),
		(SOPHOMORE, 'Sophomore'),
		(JUNIOR, 'Junior'),
		(SENIOR, 'Senior'),
	)
	
	BOY = 'B'
	GIRL = 'G'
	OPTIONS = (
		(BOY, 'Boy'),
		(GIRL, 'Girl'),
	)
	
	gender = models.CharField(max_length=1, choices=OPTIONS, null=False)
	year = models.CharField(max_length=2, choices=CHOICES, default=FRESHMAN)
	first_name = models.CharField(max_length=20, null=False)
	last_name = models.CharField(max_length=20, null=False)
	
	class Meta:
		unique_together = ('first_name', 'last_name')
		
class Record(models.Model):
	event_name = models.ForeignKey(Event, default=1)
	athlete = models.ForeignKey(Athlete, default=1)
	time_dist = models.DecimalField('Time/Distance', decimal_places=2, max_digits=5)
	date = models.DateField()
	
	class Meta:
		unique_together = ('event_name', 'athlete')
