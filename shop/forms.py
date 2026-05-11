from django import forms



class ContactForm(forms.Form):
    email = forms.EmailField()
    # form = ContactForm(data={"email": "test@example.com"})

class ProfileForm(forms.Form):
	bio = forms.CharField(required=False)
      
class TagForm(forms.Form):
	name = forms.CharField(strip=False)

class UserForm(forms.Form):
	username = forms.CharField()
	email = forms.EmailField()

class EditForm(forms.Form):
	name = forms.CharField()
	email = forms.EmailField()

class SettingsForm(forms.Form):
	timezone = forms.CharField()
	language = forms.CharField()