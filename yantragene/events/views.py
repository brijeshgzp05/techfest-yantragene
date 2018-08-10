from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.core.urlresolvers import reverse
from .models import (

	Department,
	Events,
	Coordinator,
	Participant

	)
#from accounts.models import Profile


def events_view(request):

	department = Department.objects.all()
	events = Events.objects.all()

	outer_event_list = dict()
	
	for d in department:
		
		e = events.filter(department=d)
		outer_event_list[d] = e



	context = {
		'outer_event_list':outer_event_list
	}
	
	return render(request, 'events/events.html', context)



def event_detail(request, id=None):
	
	events = get_object_or_404(Events, id=id)
	coordinator = Coordinator.objects.filter(events=events)
	
	page = events.ename.lower()
	page = 'events/'+page+'.html'

	context = {
	
		'event_title' : events.ename.upper(),
		'events' : events,
		'coordinator' : coordinator

	}
	
	return render(request, page, context)


def register_view(request):
	
	team_name = request.GET['team_name']
	member2 = request.GET['member2']
	member3 = request.GET['member3']
	member4 = request.GET['member4']
	member5 = request.GET['member5']
	event_id = request.GET['event_id']
	profile_id = request.GET['profile_id']
	events_name = request.GET['events_name']

	t = Participant.objects.filter(team_name=team_name)
	if len(t):
		return render(request, 'events/events.html', {'msg':'Team name already existed'})

	t = Participant.objects.filter(events_name=events_name, profile=profile_id)
	if len(t):
		return render(request, 'events/events.html', {'msg':'You have already participated in this event'})

	p = Participant(

		team_name=team_name,
		events_name=events_name, 
		member2=member2, 
		member3=member3,
		member4=member4,
		member5=member5,
		events_id=event_id,
		profile_id=profile_id,

		)

	p.save()

	return HttpResponseRedirect(reverse('events:events'))

