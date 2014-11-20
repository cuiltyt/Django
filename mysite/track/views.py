from django.db.models import Q
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView, CreateView
from django.core.urlresolvers import reverse
from django.utils import timezone
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect

from track.models import Athlete, Event, Record

def index(request):
	events = []
	event_names = Event.objects.values_list('event_name', flat=True).distinct()
	print event_names
	for event in event_names:
		event_number = Event.objects.filter(event_name=event).values_list('id', flat=True)[0]
		print event_number
		events += Event.objects.filter(pk=event_number)
	return render(request, 'track/index.html', { 'events' : events })
 
def AthleteList(request):
	if 'search_term' in request.GET:
		results = Athlete.objects.filter(
				Q(last_name__icontains=request.GET['search_term']) |
				Q(first_name__icontains=request.GET['search_term']))
		
		if len(results) == 1:
			url = reverse('track:athlete_profile', args=(results[0].id,))
			return redirect(url)
		else:
			return render(request, 'track/athlete_list.html', { 'athletes' : results })
	
	else:
		all = Athlete.objects.all()
		return render(request, 'track/athlete_list.html', { 'athletes' : all })

def AthleteProfile(request, athlete_id):
	records = Record.objects.filter(athlete=athlete_id)
	athlete = Athlete.objects.filter(pk=athlete_id)
	return render(request, 'track/athlete_profile.html', { 'records' : records, 'athlete' : athlete })


def EventProfile(request, event_id):
	event_profiles = []
	
	event_name = (Event.objects.get(pk=event_id)).event_name
	events = Event.objects.filter(event_name=event_name)
	
	for event in events:
		records = Record.objects.filter(event_name=event.id).order_by('time_dist')
		event_profile = { 'event' : event, 'records' : records }
		event_profiles.append(event_profile)
	print event_profiles
	return render(request, 'track/event_profile.html', { 'event_profiles' : event_profiles })

class RecordUpdate(UpdateView):
	model = Record
	template_name_suffix = '_update_form'
	fields = [ 'event_name', 'time_dist', 'date' ]

	def get_success_url(self):
		return reverse('track:athlete_profile', kwargs={ 'athlete_id': self.get_object().athlete.id })

class RecordCreate(CreateView):
	model = Record
	template_name_suffix = '_create_form'
	fields = ['athlete', 'event_name', 'time_dist', 'date' ]

	def get_initial(self):
		athlete = Athlete.objects.get(id=self.kwargs.get('pk'))
		initial = super(RecordCreate, self).get_initial()
		initial = initial.copy()
		initial['athlete'] = athlete
		return initial
	
	def get_success_url(self):
		return reverse('track:athlete_profile', kwargs={ 'athlete_id': self.get_object().id })