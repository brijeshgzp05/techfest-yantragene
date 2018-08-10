from django.shortcuts import render
from events.models import Events, Participant


# Create your views here.

def about_view(request):
	
	context = {

		'events':Events.objects.all().count(),
		'teams_paricipated':Participant.objects.all().count(),
		'prize_money':'5 00 000'
		
	}

	
	return render(request ,'aboutus/aboutus.html', context)
