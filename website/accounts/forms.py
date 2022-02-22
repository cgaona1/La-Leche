
from django import forms
from .models import Notification

class NotificationForm(forms.ModelForm):
    email = forms.EmailField(label='',
                            widget=forms.TextInput(attrs={'placeholder':'Email'}))
    remindTime = forms.IntegerField(label='',
                                    widget=forms.TextInput(attrs={'placeholder':'Time'}))
    subject = forms.CharField(label='',
                            widget=forms.TextInput(attrs={'placeholder':'Subject'}))
    message = forms.CharField(label='',
                            widget=forms.Textarea(attrs={'placeholder':'Message'}))

    class Meta:
        model = Notification
        fields = ('email', 'remindTime', 'subject', 'message')