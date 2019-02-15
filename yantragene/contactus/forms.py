from django import forms

class FeedbackForm(forms.Form):
	name = forms.CharField(label="Your name",
			widget=forms.TextInput(
					attrs={
						'class':'form-control',
						'placeholder':'Enter Your name'
					}
				)
		)

	email = forms.CharField(label="Your Email",
			widget=forms.EmailInput(
					attrs={
						'class':'form-control',
						'placeholder':'Enter Your Email'
					}
				)
		)

	review = forms.CharField(label="Your Feedback",
			widget=forms.TextInput(
					attrs={
						'class':'form-control',
						'placeholder':'Your Feedback'
					}
				)
		)