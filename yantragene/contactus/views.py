from django.shortcuts import render
from .models import Feedback
from .forms import FeedbackForm

# Create your views here.
def contactus_view(request):
	form = FeedbackForm()
	return render(request, 'contactus/contactus.html', {'form':form})

def feedback_view(request):
	
	name = request.GET['name']
	email = request.GET['email']
	review = request.GET['review']

	f1 = Feedback(name=name, email=email, review=review)
	f1.save()

	form = FeedbackForm()
	return render(request, 'contactus/contactus.html', {'form':form})
