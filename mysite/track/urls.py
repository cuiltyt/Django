from django.conf.urls import patterns, url, include
from track import views
from track.views import RecordUpdate, RecordCreate, AthleteCreate

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^athletes/', views.AthleteList, name='athlete_list'),
    url(r'^(?P<athlete_id>\d+)/', views.AthleteProfile, name='athlete_profile'),
    url(r'^edit/(?P<pk>\d+)/', RecordUpdate.as_view(), name='record_update_form'),
    url(r'^add_record/(?P<pk>\d+)/', RecordCreate.as_view(), name='record_create_form'),
    url(r'^add_athlete/', AthleteCreate.as_view(), name='athlete_create_form'),
    url(r'^events/(?P<event_id>\d+)/', views.EventProfile, name='event_profile'),
)