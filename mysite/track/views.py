from django.db.models import Q
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView, CreateView
from django.core.urlresolvers import reverse
from django.utils import timezone
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect

from track.models import Athlete, Event, Record

def index(request):
	events = Event.objects.order_by('event_name')
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
	event = Event.objects.filter(pk=event_id)
	records = Record.objects.filter(event_name=event_id).order_by('time_dist')
	return render(request, 'track/event_profile.html', { 'event' : event, 'records' : records })

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