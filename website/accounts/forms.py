
from django import forms
from .models import Notification

class NotificationForm(forms.ModelForm):
    email = forms.EmailField(label='',
                            widget=forms.TextInput(attrs={'placeholder':'Exmaple@email.com'}))
    subject = forms.CharField(label='',
                            widget=forms.TextInput(attrs={'placeholder':'Enter subject here'}))
    message = forms.CharField(label='',
                            widget=forms.Textarea(attrs={'placeholder':'Enter message here...'}))

    class Meta:
        model = Notification
        fields = ('email', 'subject', 'message')